from pypdf import PdfMerger

merger = PdfMerger()

for i in range(325, 334):
    pdf = "Berserk " + str(i) + ".pdf"
    merger.append(pdf)

merger.write("Berserk 37.cilt.pdf")
merger.close()