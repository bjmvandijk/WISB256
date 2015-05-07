#!/usr/bin/python3

import sys
import time

# Python program to ask the user for a range and display all the prime numbers in that interval

N = int(sys.argv[1])
filename = sys.argv[2]

# define output
output = open(filename, 'w')

count = 2
s = set(range(2, N))

# start timing
T1 = time.perf_counter()

# select numbers 
for num in range(2, N):
    i = 2
    # remove all numbers which are not prime numbers
    while num*i <= N:
        if num*i in s:
            s.remove(num*i)
            count += 1
        i += 1    

# show all prime number in set
results = map(lambda x: x, s)

# display the results
for result in results:
    output.write(str(result) + '\n')    

# end timing
T2 = time.perf_counter()
print('Found ', (N - count), ' Prime numbers smaller than ', N, ' in ', T2 - T1, 'sec.')
output.write(str('Found ') + str(N - count) + str(' Prime numbers smaller than ') + str(N) + str(' in ') + str(T2 - T1) + str(' sec.'))
