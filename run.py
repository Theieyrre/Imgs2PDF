from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def add_image(image_path):
    my_canvas = canvas.Canvas("canvas_image.pdf", pagesize=letter)
    my_canvas.drawImage(image_path, x=0, y=0)
    my_canvas.save()

if __name__ == '__main__':
    image_path = 'school.png'
    add_image(image_path)