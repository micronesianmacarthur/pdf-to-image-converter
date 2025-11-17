# 🖼️ PDF to Image Converter (PyMuPDF)
This project is a command-line tool that converts PDF files to images (png format) using PyMuPDF.

## Project Summary
The purpose of this project is to minimize the effort to convert PDF files to images.

### Key Features:
- Scans and processes all .pdf files found in a specified source path.
- Creates a new directory named `"Images"` in the same directory as the source path.
- Incorporates a command-line progress bar using `sys.stdout.write()`.

The `main.py` script calls the `convert_pdf_to_image()` function from the `tool.py` script. The progress bar is called from `progress_bar.py` inside the `convert_pdf_to_image()` function.

The output images will be named the same name as the PDF file.

**Caution**

If the source PDF file contains multiple pages, the output image will be the same name therefore overriding the previous image, which may not be the intended behavior.

You may modify the `convert_pdf_to_image()` function inside the `tool.py` file to include the page number in the output image name.

```python
def convert_pdf_to_image():
    # ... previous code ...
        for page in doc:  # iterate through the pages
            # ... previous code ...
            pix.save(f"{export_path}/{filename.split('.')[0]}.png")
```

## Installation
Follow these steps to use or modify the project to your needs.

1. Clone the repository to your local machine.

```bash
git clone <repo-url>
cd pdf-to-image-converter
```

2. Install the Python Dependencies

```bash
pip install pymupdf
```

3. Currently, the source path is hardcoded in the `tool.py` file inside the `get_pdf_path()` function. Modify the source path to your needs.

```python
def get_pdf_path():
    pdf_dir = "your/source/path/"
```

4. Run the script.

```bash
python main.py
```

## Future Improvements
- Modify the code to accept user input for the source path, export path, and image output name.
- Add a GUI to the tool.