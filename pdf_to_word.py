import pdfplumber
from docx import Document

def pdf_to_docx(pdf_file, docx_file):
    with pdfplumber.open(pdf_file) as pdf:
        page_text = ''
        for page_number, page in enumerate(pdf.pages):
            page_text += page.extract_text()
            print(page_text)


    doc = Document()
    doc.add_paragraph(page_text)
    doc.save(docx_file)

pdf_to_docx("input2.pdf", "output.docx")
