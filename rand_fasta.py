#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>


def rand_dna(len, a, c, g, t):
    seq = []
    for i in range(len):
        r = random.random()
        if r < a:
            seq.append('A')
        elif r < a + c:
            seq.append('C')
        elif r < a + c +g:
            seq.append('G')
        else:
            seq.append('T')
    return ''.join(seq)




count = int(sys.argv[1])
min = int(sys.argv[2])
max = int(sys.argv[3])
a_freq = float(sys.argv[4])
c_freq = float(sys.argv[5])
g_freq = float(sys.argv[6])
t_freq = float(sys.argv[7])


for i in range(count):
    x = random.randint(min, max)
    dna = rand_dna(x, a_freq, c_freq, g_freq, t_freq)
    print(f'>{i}')
    print(dna)


"""

"""
