import sys, os
from PDFCreator import PDFCreator
from glob import glob

from pypdf import PdfWriter


def main():
    merger = PdfWriter()
    main_dir = sys.argv[1]
    save_dir = sys.argv[2]
    for dir in glob(main_dir + "/*/"):
        filename = dir.split("\\")[-2] + ".pdf"
        filename = os.path.join(save_dir, filename)
        pdf_c = PDFCreator(filename)
        pdf_c.read_images(dir)
        merger.append(filename)

    main_file = main_dir.split("\\")[-1]
    merger.write(save_dir + "\\" + main_file + ".pdf")
    merger.close()


if __name__ == "__main__":
    main()
