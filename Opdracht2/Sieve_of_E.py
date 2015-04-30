#!/usr/bin/python3

import sys
import time

# Python program to ask the user for a range and display all the prime numbers in that interval

N = int(sys.argv[1])
filename = sys.argv[2]

# define output
output = open('prime.dat', 'w')

count = 0

# start timing
T1 = time.perf_counter()

# select and print prime numbers
for num in range(1, N):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           output.write(str(num) + '\n')
           count += 1

# end timing
T2 = time.perf_counter()
print('Found ', count, ' Prime numbers smaller than ', N, ' in ', T2 - T1, 'sec.')
output.write(str('Found ') + str(count) + str(' Prime numbers smaller than ') + str(N) + str(' in ') + str(T2 - T1) + str(' sec.'))


