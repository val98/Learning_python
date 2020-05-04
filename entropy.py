#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import math
import sys
import fileinput

file = sys.argv[1]
data = []
columns = []
h = 0
sum = 0

for line in fileinput.input(file):
    if line[0] == '#':
        continue
    else:
        line = line.rstrip()
        columns = line.split()
        value = float(columns[1])
        assert(value < 1 and value > 0)
        data.append(float(columns[1]))
        sum = sum + value
assert(sum == 1)
#print(data)

for i in range(len(data)):
    h += data[i] * math.log2(data[i])
    #h = h * (-1)
print('%3f' % (-h))



"""
python3 entropy.py nucleotides.txt
1.846
"""
