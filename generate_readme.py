import sys
import PyPDF2
import argparse
import subprocess

def insert_data(rPath, ques_line, data):
    lines = open(rPath, 'r').readlines()
    lines[ques_line] = data
    out = open(rPath, 'w')
    out.writelines(lines)
    out.close()

def make_readme(ques1_content, ques2_content, rPath):
	identifier = '## Questions'
	try:
		g1=subprocess.Popen(
			["grep", "-n", "^{}".format(identifier), rPath], 
			stdout=subprocess.PIPE)
		g2=subprocess.Popen(
			["grep", "-Eo", "^[^:]+"], 
			stdout=subprocess.PIPE, stdin=g1.stdout, encoding='utf-8')
		
		ques_line = g2.communicate()[0]

		data = 'Ques. 1. {}\n---\nQues. 2. {}'.format(ques1_content, ques2_content)
		insert_data(rPath, int(ques_line), data)

		return 'Success'
	except ValueError:
		return 'This file does not have the identifier: {}'.format(identifier)

def get_ques_content(ques1, ques2, pPath, content=[]):
	main1=subprocess.Popen(
		["pdftotext", "-layout", "-nopgbrk", pPath, "-"],
		stdout=subprocess.PIPE)

	g1=subprocess.Popen(
		["perl", "-ne", "if(/^(?:Ques\\. |Q)(\\d+)\\.\\s+(.*)/){{$q=$1=={};$_=$2.'\\n';}} print if $q;".format(ques2)],
		stdout=subprocess.PIPE, stdin=main1.stdout, encoding='utf-8')
	ques1_content = g1.communicate()[0]

	main2=subprocess.Popen(
		["pdftotext", "-layout", "-nopgbrk", pPath, "-"],
		stdout=subprocess.PIPE)	

	g2=subprocess.Popen(
		["perl", "-ne", "if(/^(?:Ques\\. |Q)(\\d+)\\.\\s+(.*)/){{$q=$1=={};$_=$2.'\\n';}} print if $q;".format(ques1)],
		stdout=subprocess.PIPE, stdin=main2.stdout, encoding='utf-8')
	ques2_content = g2.communicate()[0]

	return ques1_content, ques2_content

def generate_txt(pdf_file_path):
	txt_file_path='./snaps/'+pdf_file_path[:-4]+'.txt'
	with open(pdf_file_path, 'rb') as pdf_file, open(txt_file_path, 'w') as txt_file:
		read_pdf = PyPDF2.PdfFileReader(pdf_file)
		number_of_pages = read_pdf.getNumPages()
		for page_number in range(number_of_pages):
			page = read_pdf.getPage(page_number)
			page_content = page.extractText()
			txt_file.write(page_content)
	return txt_file_path

def get_ques_num(tPath, year, section, roll):
	g1=subprocess.Popen(
		["grep", "-A2", "RK{}{}".format(year[-2:], section), tPath], 
		stdout=subprocess.PIPE)
	g2=subprocess.Popen(
		["grep", "-A4", "-P", "[A-Z]{}[,\\s\\n\\x0]".format(roll)], 
		stdout=subprocess.PIPE, stdin=g1.stdout)
	g3=subprocess.Popen(
		["grep", "-m", "1", "[[:digit:]],[[:digit:]]"], 
		stdout=subprocess.PIPE, stdin=g2.stdout, encoding='utf-8')
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
	ques1, ques2 = get_ques_num(
		tPath, 
		args['year'], 
		args['section'], 
		args['roll']
	)

	ques1_content, ques2_content = get_ques_content(
		ques1, 
		ques2, 
		args['pPath']
	)

	task = make_readme(
		ques1_content,
		ques2_content,
		args['rPath']
	)

	print(task)

	return 0

if __name__ == "__main__": sys.exit(main())
