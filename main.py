# main.py

from tool import convert_pdf_to_image


def main():
    print("Hello from pdf-to-image-converter!")
    try:
        print("Converting PDF to image...")
        convert_pdf_to_image()
        print("PDF to image conversion completed successfully.")
    except Exception as e:
        print("Conversion failed.")
        print(e)


if __name__ == "__main__":
    main()
