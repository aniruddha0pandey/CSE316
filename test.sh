#!/bin/bash

year=2017
section=BN
# match_line=$(grep -A2 "RK${year: -2}$section" ./ListOfQuestions_K17BN.txt | grep -A4 ".$roll_no" | grep -m 1 -n '[[:digit:]],[[:digit:]]' | grep -Eo '^[^:]+')
# last_line=$(grep -A2 "RK${year: -2}$section" ./ListOfQuestions_K17BN.txt | wc -l | grep -Eo '^[^:]+')

for var in 01 28 53 02 29 54 03 30 55 04 31 56 05 32 57 06 33 58 07 34 59 08 73 60 09 75 61 10 35 62 11 36 63 12 37 64 13 38 65 14 39 66 15 40 67 16 41 68 17 42 18 43 19 44 20 45 21 46 22 47 23 48 24 49 25 50 26 51 27 52
do
	echo "$var: $(grep -A2 "RK${year: -2}$section" ./ListOfQuestions_K17BN.txt | grep -A4 -P "[A-Z]$var[,\s\n\x0]" | grep -m 1 '[[:digit:]],[[:digit:]]')"
done