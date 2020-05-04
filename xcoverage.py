#!/usr/bin/env python3

# Write a program that simulates random BAC coverage over a genome
# Command line arguments include
# 	Genome size (e.g. 1000)
# 	X coverage (e.g. 5)
# Use assert() to check parameter bounds
# Report min, max, and histogram of coverage
# Note that your output may vary due to random function

import sys
import random

assert(len(sys.argv) == 3)
bins = int(sys.argv[1])
coverage = int(sys.argv[2])
assert(bins > 0)
assert(coverage > 0)

genome = [0]* bins
bacs = bins * coverage
for i in range(bacs):
    r = random.randint(0, bins-1)
    genome[r]+=1

#print(genome)
genome.sort()
max = genome[-1]
min = genome[0]

histogram = [0]* (max+1)
for c in genome:
    histogram[c]+=1


print('Size:', bins)
print('X:', coverage)
print('BACs:',bacs)
print('Min:', min)
print('Max:', max)
print('Count:')
for k in range(len(histogram)):
   print(k, histogram[k])




"""
Size: 1000
X: 5.0
BACs: 5000
Min: 0
Max: 13
Counts:
0 5
1 39
2 88
3 144
4 175
5 150
6 151
7 116
8 59
9 40
10 20
11 5
12 6
13 2
"""
