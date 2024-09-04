# jpg-trimmer
This repository contains a Python script that trims white borders from JPG images by removing the excess whitespace from the left, right, top, and bottom of the image.

## Prerequisites

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Installation

Follow these steps to set up the environment and install the required dependencies:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To trim the borders of an image, run the following command:

```bash
python app.py <folder-images-path> <output-folder-image-path>
```

Replace `<folder-images-path>` with the path to the JPG image you want to process.

The script will output the trimmed image in the same directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute by opening an issue or submitting a pull request.
