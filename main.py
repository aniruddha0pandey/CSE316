import sys
from PyPDF2 import PdfFileReader

def text_extractor(input_file, total_pages):
    with input_file as f:
        pdf = PdfFileReader(f)

        page = pdf.getPage(total_pages - 1)
        print(page)
        print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)


def main(args=None):
    path = './ListOfQuestions_K17BN.pdf'
    input_file = open(path, "rb")
    total_pages = PdfFileReader(input_file).getNumPages()
    text_extractor(input_file, total_pages)

if __name__ == '__main__': sys.exit(main())
