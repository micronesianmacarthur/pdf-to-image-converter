# tool.py

import os
import pymupdf
from progress_bar import print_progress_bar


def convert_pdf_to_image():
    files = get_pdf_path()
    files_dirname = os.path.dirname(files[0])
    export_path = os.path.join(files_dirname, "Images")
    try:
        os.mkdir(os.path.join(export_path))
    except FileExistsError:
        pass
    for i, file in enumerate(files):
        filename = os.path.basename(file)
        doc = pymupdf.open(file)  # open document
        for page in doc:  # iterate through the pages
            print_progress_bar(i + 1, len(files), prefix='Progress:', suffix='Complete', length=50)
            pix = page.get_pixmap()  # render page to an image
            pix.save(f"{export_path}/{filename.split('.')[0]}.png")  # store image as a PNG


def get_pdf_path():
    pdf_dir = "/mnt/hdd/ARCHIVE/Downloads/Documents/ARISE/" # Modify this path to your needs

    pdf_files = os.listdir(pdf_dir)
    
    path_to_pdf = []

    for pdf in pdf_files:
        if pdf.endswith(".pdf"):
            path_to_pdf.append(os.path.join(pdf_dir, pdf))

    return path_to_pdf