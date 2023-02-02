from pdf2docx import parse

pdf_file = 'test.pdf'
docx_file = 'test.docx'

# convert pdf to docx
parse(pdf_file, docx_file, start=0, end=None)