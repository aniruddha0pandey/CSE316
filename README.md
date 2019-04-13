# CSE316

```
$ pip install PyPDF2 pillow pdf2image
$ python main.py
```
```
$ For Unix bases systems
$ sudo apt install poppler-utils
$ # For Windows
$ # Download binaries from http://blog.alivate.com.au/poppler-windows/
```


## Known Bugs
- Registration Number `68` is showing wrong question number. Dude to Form Feed (FF) line ending due to separation of pages and tables to next page.
- Question number `11, 12, 13, 14, 15 , 16, 17` images aren't generating. grep isn't able to recognize question number as the the Line Feed (LL) line ending character is coming after the first digit of the above specified range.
- The snap generated contain

Possible solution: Port to Poppler utilities like `pdftotext`, `pdftoimage`.