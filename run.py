import sys, os
from glob import glob

from tqdm import tqdm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


def main():
    path = sys.argv[1]
    filename = sys.argv[2]
    c = canvas.Canvas(filename, pagesize=A4)

    imgs = []
    for file in glob(os.path.join(path, "*.*g")):
        imgs.append(file)

    imgs.sort()

    for img in tqdm(imgs):
        c.drawImage(img, 0, 0, width=210*mm, height=298*mm)
        c.showPage()
    del imgs

    c.save()

if __name__ == '__main__':
    main()