from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from natsort import natsorted

from tqdm import tqdm
from glob import glob
import os


class PDFCreator:
    def __init__(self, filename) -> None:
        self.canvas = canvas.Canvas(filename, pagesize=A4)

    def read_images(self, directory):
        imgs = []
        for file in tqdm(glob(os.path.join(directory, "*.*g")), desc="Reading Images"):
            imgs.append(file)
        imgs = natsorted(imgs)
        self.add_images(imgs)

    def add_images(self, imgs):
        for img in tqdm(imgs, desc="Creating PDF file from images"):
            self.canvas.drawImage(img, 0, 0, width=210 * mm, height=298 * mm)
            self.canvas.showPage()
        self.canvas.save()
