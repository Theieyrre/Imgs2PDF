import sys


from tqdm import tqdm

from PDFCreator import PDFCreator

def main():
    path = sys.argv[1]
    filename = sys.argv[2]
    pdf_c =  PDFCreator(filename)
    pdf_c.read_images(path)

if __name__ == '__main__':
    main()