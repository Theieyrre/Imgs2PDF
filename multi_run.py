import sys, os
from PDFCreator import PDFCreator
from glob import glob


def main():
    main_dir = sys.argv[1]
    save_dir = sys.argv[2]
    for dir in glob(main_dir + "/*/"):
        filename = dir.split("\\")[-2] + ".pdf"
        filename = os.path.join(save_dir, filename)
        pdf_c = PDFCreator(filename)
        pdf_c.read_images(dir)


if __name__ == "__main__":
    main()
