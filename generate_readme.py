import sys
import PyPDF2
import argparse
import subprocess

from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def generate_snaps(pPath, ques1_num, ques2_num):
   #  with open(pPath, 'rb') as pdf_file:
   #      read_pdf = PyPDF2.PdfFileReader(pdf_file)
   #      number_of_pages = read_pdf.getNumPages()
   #      for page_number in range(number_of_pages):
   #          page = read_pdf.getPage(page_number)
   #          page_content = page.extractText()
			# main=subprocess.Popen(
			# 	["grep"],
			# 	stdout=subprocess.PIPE, stdin=page_content, encoding='utf-8')
			# out, err = main.communicate()[0]
			# if not err: f_page = page_number + 1

	ques1={'num': ques1_num, 'f_page': 7, 'l_page': 7}
	ques2={'num': ques2_num, 'f_page': 14, 'l_page': 14}

	for q in ques1, ques2:
		convert_from_path(
		 	pPath,
		 	output_folder="./snaps/",
		 	output_file='ques{}'.format(q['num']),
		 	first_page=q['f_page'],
		 	last_page=q['l_page'],
		 	fmt='png'
		)

	img_ratio_width, img_ratio_height = 17, 22
	img_data = '<details><summary>Question Page Snapshots</summary><br />\
	<img src="./snaps/ques{q_no1}-0{q_no_pg1}.png" alt="Ques 1 Image" width="{wid}" height="{hei}" border="10" /> \
	<img src="./snaps/ques{q_no2}-{q_no_pg2}.png" alt="Ques 2 Image" width="{wid}" height="{hei}" border="10" />\
	</details>'.format(
		q_no1=ques1['num'], 
		q_no_pg1=ques1['f_page'],
		q_no2=ques2['num'],
		q_no_pg2=ques2['f_page'],
		wid=(img_ratio_width*25),
		hei=(img_ratio_height*25)
	)

	return img_data, 'Success Img Generated'


def insert_txt(rPath, identifier, ques1_content, ques2_content, img_data):
	try:
		g1=subprocess.Popen(
			["grep", "-n", "^{}".format(identifier), rPath], 
			stdout=subprocess.PIPE)
		g2=subprocess.Popen(
			["grep", "-Eo", "^[^:]+"], 
			stdout=subprocess.PIPE, stdin=g1.stdout, encoding='utf-8')
		ques_line = g2.communicate()[0]
		txt_data = '```\nQues. 1. {}\n---\nQues. 2. {}```'.format(ques1_content, ques2_content)
		data = '{}\n\n{}\n'.format(img_data, txt_data)
		message = 'Success Txt Insert'
	except ValueError:
		return 'This file does not have the identifier: {}'.format(identifier)

	lines = open(rPath, 'r').readlines()
	lines[ int(ques_line) ] = data
	out = open(rPath, 'w')
	out.writelines(lines)
	out.close()

	return message


def make_readme(ques1, ques2, pPath, rPath, identifier):
	img_data, msgimg = generate_snaps(pPath, ques1['num'], ques2['num'])
	msgtxt = insert_txt(rPath, identifier, ques1['content'], ques2['content'], img_data)
	return '{} | {}'.format(msgimg, msgtxt)


def get_ques_content(ques1_num, ques2_num, pPath, content=[]):
	main2=subprocess.Popen(
		["pdftotext", "-layout", "-nopgbrk", pPath, "-"],
		stdout=subprocess.PIPE)	
	g2=subprocess.Popen(
		["perl", "-ne", "if(/^(?:Ques\\. |Q)(\\d+)\\.\\s+(.*)/){{$q=$1=={};$_=$2.'\\n';}} print if $q;".format(ques2_num)],
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
	
	return g3.communicate()[0].replace('\n', '').split(',')


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
	rPath = args['rPath']
	pPath = args['pPath']
	tPath = generate_txt( pPath )

	ques1_num, ques2_num = get_ques_num(
		tPath, 
		args['year'], 
		args['section'], 
		args['roll']
	)

	ques1_content, ques2_content = get_ques_content(
		ques1_num, 
		ques2_num, 
		pPath
	)

	ques1={'num': ques1_num, 'content': ques1_content}
	ques2={'num': ques2_num, 'content': ques2_content}
	identifier = input("Enter identifier(default '## Questions'): ") or '## Questions'
	task = make_readme(
		ques1,
		ques2,
		pPath,
		rPath,
		identifier	
	)

	print(task)
	
	return 0


if __name__ == "__main__": sys.exit(main())
