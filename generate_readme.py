import sys
import PyPDF2
import argparse
import subprocess
import subprocess

def generate_txt(pdf_file_path):
	text_file_path='./snaps/'+pdf_file_path[:-4]+'.txt'
	with open(pdf_file_path, 'rb') as pdf_file, open(text_file_path, 'w') as text_file:
		read_pdf = PyPDF2.PdfFileReader(pdf_file)
		number_of_pages = read_pdf.getNumPages()
		for page_number in range(number_of_pages):
			page = read_pdf.getPage(page_number)
			page_content = page.extractText()
			text_file.write(page_content)
	return text_file_path

def get_ques(tPath, year, section, roll):
	g1=subprocess.Popen(
		["grep", "-A2", "RK{}{}".format(year[-2:], section), tPath], 
		stdout=subprocess.PIPE)
	g2=subprocess.Popen(
		["grep", "-A4", "-P", "[A-Z]{}[,\\s\\n\\x0]".format(roll)], 
		stdout=subprocess.PIPE, stdin=g1.stdout)
	g3=subprocess.Popen(
		["grep", "-m", "1", "[[:digit:]],[[:digit:]]"], 
		stdin=g2.stdout, stdout=subprocess.PIPE, encoding='utf-8 ')
	return g3.communicate()[0].split(',')

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("pPath", 
		help="Path for PDF file to be render")
	parser.add_argument("rPath", 
		help="Path for README.md to be generated")
	parser.add_argument("-y", "--year", nargs='?', 
		help="Batch year of admission")
	parser.add_argument("-s", "--section", nargs='?', 
		help="Class section")
	parser.add_argument("-r", "--roll", nargs='?', 
		help="Roll Number")

	return vars(parser.parse_args())	

def main():
	args = get_args()
	tPath = generate_txt(args['pPath'])
	ques1, ques2 = get_ques(tPath, args['year'], args['section'], args['roll'])
	return 0

if __name__ == "__main__": sys.exit(main())
