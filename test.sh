#!/bin/bash

year=2017
section=BN
input_file_path=./snaps/ListOfQuestions_K17BN.txt
# match_line=$(grep -A2 "RK${year: -2}$section" ./ListOfQuestions_K17BN.txt | grep -A4 ".$roll_no" | grep -m 1 -n '[[:digit:]],[[:digit:]]' | grep -Eo '^[^:]+')
# last_line=$(grep -A2 "RK${year: -2}$section" ./ListOfQuestions_K17BN.txt | wc -l | grep -Eo '^[^:]+')
# for page_no in $(seq 1 22); do echo $(pdftotext -layout -nopgbrk -f $page_no -l $page_no ./ListOfQuestions_K17BN.pdf - | grep 'Ques\.'); done

for var in 01 28 53 02 29 54 03 30 55 04 31 56 05 32 57 06 33 58 07 34 59 08 73 60 09 75 61 10 35 62 11 36 63 12 37 64 13 38 65 14 39 66 15 40 67 16 41 68 17 42 18 43 19 44 20 45 21 46 22 47 23 48 24 49 25 50 26 51 27 52
do
	echo "$var: $(grep -A2 "RK${year: -2}$section" $input_file_path | grep -A4 -P "[A-Z]$var[,\s\n\x0]" | grep -m 1 '[[:digit:]],[[:digit:]]')"
done

# pdftotext -layout -nopgbrk ./ListOfQuestions_K17BN.pdf - | grep "^Q.*"
# Ques. 1. Considering 4 processes with the arrival time and the burst time requirement of the
# Ques. 2. Considering the arrival time and burst time requirement of the process the scheduler
# Ques. 3. Consider a scheduler which schedules the job by considering the arrival time of the
# Ques. 4. Consider a scheduling approach which is non pre-emptive similar to shortest job next in
# Ques. 5. CPU schedules N processes which arrive at different time intervals and each process is
# Ques. 6. Design a scheduling program that is capable of scheduling many processes that comes
# Ques. 7. Design a scheduling program to implements a Queue with two levels:
# Ques. 8. Sudesh Sharma is a Linux expert who wants to have an online system where he can
# Ques. 9. Design a scheduler that uses a preemptive priority scheduling algorithm based on
# Ques. 10. Design a scheduler with multilevel queue having two queues which will schedule the
# Ques. 11. Reena's operating system uses an algorithm for deadlock avoidance to manage the
# Ques. 12. Three students (a, b, c) are arriving in the mess at the same time. The id numbers of
# Ques. 13. Write a program for multilevel queue scheduling algorithm. There must be three
# Ques. 14. Write a program to implement priority scheduling algorithm with context switching
# Ques. 15. A uniprocessor system has n number of CPU intensive processes, each process has its
# Ques. 16. Design a scheduler that can schedule the processes arriving system at periodical
# Ques. 17. Design a scheduler following non-preemptive scheduling approach to schedule the
# Ques. 18. Ten students (a,b,c,d,e,f,g,h,i,j) are going to attend an event. There are lots of gift
# Ques. 19. There are 5 processes and 3 resource types, resource A with 10 instances, B with 5
# Ques. 20. Consider that a system has P resources of same type. These resources are shared by Q
# Ques. 21. Consider a scenario of demand paged memory. Page table is held in registers. It takes
# Ques. 22. Consider following and Generate a solution to find whether the system is in safe state
# Ques. 23. Write a multithreaded program that implements the banker's algorithm. Create n
# Ques 24. Design a scheduling program to implements a Queue with two levels:
# Ques 25. Write a program for multilevel queue scheduling algorithm. There must be three queues
# Ques 26. Write a program in C which will accept5 positive integers as command line
# Ques 27. Write a program in C which reads input CPU bursts from a the first line of a text file
# Ques 28. Given five memory partitions of 100 KB, 500 KB, 200 KB, 300 KB, and 600 KB
# Ques 29. Write a C program to create a page table for a program of 5MB. Consider page size
# Ques 30. Write a C program to solve the following problem:
# Q31. Write a C program to solve the following problem:
# Q32. Write a C program to solve the following problem:
# Q33. Write a C program to solve the following problem:
# Q34. Write a C program to solve the following problem:
# Q35. Write a C program to solve the following problem:
# Q36. Consider the following set of processes, with the length of the CPU burst given in
# Q37. Consider the following four processes, with the length of the CPU burst given in
# Q38. consider the following set of processes, assumed to have arrived at time 0, in the
# Q39.Thereare five processes in the system. All five processes arrive at time 0, in the order
# Q40. Consider the following set of processes, with the length of the CPU burst given in
# Q41. Write a program which incorporate Peterson's solution for synchronizing two processes
# Q42. The Sleeping-Barber Problem. A barbershop consists of a waiting room with n chairs
# Q43. Develop a scheduler which submits processes to the processor in the following
# Q44. Develop a scheduler which submits processes to the processor in the following scenario
# Q45.If a teacher is being served and during the period when he is being served another
# Q46.Consider a scheduling approach which is nonpre-emptive similar to shortest job next in
# Q47. For SJF algorithm,
# Q48.CPU schedules N processes which arrive at different time intervals and each process is
# Q49.Design a scheduling program that is capable of scheduling many processes that comes in at
# Q50. Design a scheduling program to implements a Queue with two levels:
# Q51. Design a scheduler that uses a pre-emptive priority scheduling algorithm based on
# Q52.Design a scheduler with multilevel queue having two queues which will schedule the
# Q53.consider a system with five processes P0 through P4 and three resource types A, B and C.
# Q54. ASSIGNMENT COMPLETION PROBLEM