import os
import sys
from PIL import Image, ImageOps
import numpy as np

def trim_image(image_path):
    try:
        image = Image.open(image_path)
        # Convert image to grayscale to focus on non-white areas
        gray_image = image.convert("L")
        
        # Convert to numpy array
        np_image = np.array(gray_image)
        
        # Invert the image (so that white becomes black and vice versa)
        inverted_np_image = np.invert(np_image)
        
        # Get the bounding box of the non-black areas (which were white in the original image)
        non_zero_columns = np.where(inverted_np_image.max(axis=0) > 0)[0]
        non_zero_rows = np.where(inverted_np_image.max(axis=1) > 0)[0]
        
        # Determine the cropping box
        crop_box = (min(non_zero_columns), min(non_zero_rows), max(non_zero_columns), max(non_zero_rows))
        
        # Crop the image
        cropped_image = image.crop((crop_box[0], crop_box[1], crop_box[2]+1, crop_box[3]+1))
        
        return cropped_image
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def main(input_folder, output_folder):
    # Validate the input folder
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        sys.exit(1)
    
    # Ensure the output folder exists
    if not os.path.isdir(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as e:
            print(f"Error: Unable to create output folder '{output_folder}': {e}")
            sys.exit(1)
    
    # Process each JPG file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)
            
            trimmed_image = trim_image(input_file_path)
            if trimmed_image:
                try:
                    trimmed_image.save(output_file_path)
                    print(f"Processed and saved: {output_file_path}")
                except Exception as e:
                    print(f"Error saving file '{output_file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py InputFolder OutputFolder")
        print("Example: python app.py /ruta/a/InputFolder /ruta/a/OutputFolder")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    main(input_folder, output_folder)
