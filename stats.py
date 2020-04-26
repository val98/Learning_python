#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

import fileinput
import math

p = []
count = 0
#get values from file
for line in fileinput.input():
    if line.startswith('#'): continue
    else:
        count = count +1
        number = line.split()
        number = float(number[0])
        p.append(number)


min = p[0]
max = p[0]
sum = 0
previousValue = p[0]
# find min, max, and mean
for value in p:
    if value < min:
        min = value
    if value > max:
        max = value
    sum = sum + value

mean = sum/ count


#Find Standard Deviation

sumOfDifferences =0
for value in p:
    difference = (value - mean)**2
    sumOfDifferences = sumOfDifferences + difference
std = sqrt(sumOfDifferences/len(p))


#Find Median
medianVal = 0
newMin = p[0]
place = 0
if count%2 == 0:
    for i in range(int(count/2)+1):
        for j in range(count):
            if p[j] < newMin:
                newMin = p[j]
                place = j
        p[place] = max
        if i == int(count/2)-1:
            medianVal = newMin
        if i == int(count/2):
            medianVal = (medianVal+ newMin)/2
        newMin = max


else:
    for i in range(int(count/2)):
        for j in range(count):
            if p[j] < newMin:
                newMin = p[j]
                place = j
        p[place] = max
        if i == int(count/2)-1:
            medianVal = newMin
        newMin = max



print("Count: ", count)
print("Minimum: ", min)
print("Maximum: ", max)
print("Mean: ", mean)
print("Std. dev: ", std)
print("Median: ", medianVal)

"""
h = 0
for i in range(len(p)):
    h -= p[i] * math.log2(p[i])
print('%.3f' % (h))
"""

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
