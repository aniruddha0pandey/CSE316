from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path(
		 	'./ListOfQuestions_K17BN.pdf',
		 	output_folder="./snaps/",
		 	first_page=7,
		 	last_page=8,
		 	fmt='png'
	)