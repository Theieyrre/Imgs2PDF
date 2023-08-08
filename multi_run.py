import sys, os
from PDFCreator import PDFCreator

def main():
    main_dir = sys.argv[1]
    for i in range(1, 37):
        pre_filename = "Berserk " + str(i) + ".cilt"
        filename = pre_filename + ".pdf"
        path = os.path.join(main_dir, pre_filename)
        pdf_c = PDFCreator(filename)
        pdf_c.read_images(path)

if __name__ == '__main__':
    main()