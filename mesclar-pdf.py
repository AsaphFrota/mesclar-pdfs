import PyPDF2
import os

merger = PyPDF2.PdfFileManager()

lista_arquivos = os.listdir("pdfs-mesclar")
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"pdfs-mesclar/{arquivo}")

merger.write("PFF-final.pdf")