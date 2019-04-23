# CSE316

```shell
$ pip install PyPDF2 pillow pdf2image
$ python generate_readme.py ./ListOfQuestions_K17BN.pdf ./README.md -y 2017 -s BN -r 10
```
```shell
$ For Unix bases systems
$ sudo apt install poppler-utils
$ # For Windows
$ # Download binaries from http://blog.alivate.com.au/poppler-windows/
```

## Questions
Ques. 1. Consider the following four processes, with the length of the CPU burst given in
\nmilliseconds

Write a C program to calculate average waiting time using shortest-remaining-time-first
scheduling.

---
Ques. 2. Design a scheduler with multilevel queue having two queues which will schedule the
\n
processes on the basis of pre-emptive shortest remaining processing time first algorithm (SROT)

followed by a scheduling in which each process will get 2 units of time to execute. Also note that

queue 1 has higher priority than queue 2. Consider the following set of processes (for

reference)with their arrival times and the CPU burst times in milliseconds.

-------------------------------------

Process Arrival-Time Burst-Time

-------------------------------------

P1         0  5

P2         1  3

P3         2  3

P4         4  1

-------------------------------------

Calculate the average turnaround time and average waiting time for each process. The input for

number of processes and their arrival time, burst time should be given by the user.

## Known Bugs
- Registration Number `68` is showing wrong question number. Dude to Form Feed (FF) line ending due to separation of pages and tables to next page.
- Question number `11, 12, 13, 14, 15 , 16, 17` images aren't generating. grep isn't able to recognize question number as the the Line Feed (LL) line ending character is coming after the first digit of the above specified range.
- Inefficient implementation on piping pdftotext output to perl process. Possible soultion: save the converted file other thatn buffer.
- Text file is generating twice implying bad design. Possible solution: unify txt generation from PyPDF2 and pdftotext.

Possible solution: Port to Poppler utilities like `pdftotext`, `pdftoimage`.