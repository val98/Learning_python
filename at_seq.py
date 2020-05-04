#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

dna = ''
len = 30
count = 0


for i in range(len):
    r = random.random()

    if r <= .60:
        s = random.random()
        if s < 0.5:
            dna += ('A')
            #count += count
        else:
            dna += ('T')
            #count += count
    else:
        s = random.random()
        if s < 0.5:
            dna += ('C')
        else:
            dna += ('G')

for i in range(len):
    if (dna[i] == 'A') or (dna[i] == 'T'):
        count = count + 1

print(len, count/30, dna)




"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
