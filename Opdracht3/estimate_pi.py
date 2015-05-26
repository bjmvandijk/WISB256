#!/usr/bin/python3

import math
import random
import sys


# voorwaarde 1 en 2
if len(sys.argv) < 3:
    print('Use: estimate_pi.py N L')
    exit(3)

N = int(sys.argv[1])
L = float(sys.argv[2])

# voorwaarde 3
if L > 1:
    print('AssertionError: L should be smaller than 1') 
    exit(1)

# voorwaarde 4
if len(sys.argv) > 3:
	seed = float(sys.argv[3])
	random.seed(seed)

def drop_needle(L):
	x0 = random.random()
	a = random.vonmisesvariate(0, 0)
	x = x0 + L*math.cos(a)
	return abs(math.floor(x))

hits = 0
for i in range(0, N):
	hits += drop_needle(L)

print(str(hits) + ' hits in ' + str(N) + ' tries')
print('Pi =', (2*N*L / hits))
