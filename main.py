import sys
from PyPDF2 import PdfFileReader

def extract(pdf_file_path, text_file_path):
    with open(pdf_file_path, 'rb') as pdf_file, open(text_file_path, 'w') as text_file:
        read_pdf = PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            text_file.write(page_content)
            print(page_number + 1)

def main(args=None):
    pdf_file_path = './ListOfQuestions_K17BN.pdf'
    text_file_path = './ListOfQuestions_K17BN.txt'
    extract(pdf_file_path, text_file_path)
    return 0

if __name__ == '__main__': sys.exit(main())
