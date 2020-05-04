#!/usr/bin/env python3

# Create a program that generates random sequences in FASTA format
# Each name should be unique
# Length should have a minimum and maximum
# GC% should be a parameter
# Use assert() to check bounds of command line values
# When creating sequences, append and join
# Command line:
#	python3 rand_seq.py <# of seqs> <min> <max> <gc>

import sys
import random
assert(len(sys.argv) == 5)

numSeqs = int(sys.argv[1])
min = int(sys.argv[2])
max = int(sys.argv[3])
gc = float(sys.argv[4])

for i in range(numSeqs):
    sequence = []
    length = random.randint(min, max)

    for j in range(length):
        random_percentage = random.random()
        if random_percentage < gc:
            random_gc = random.random()
            if random_gc < .50:
                sequence.append('C')
            else:
                sequence.append('G')
        else:
            random_at = random.random()
            if random_at < .50:
                sequence.append('A')
            else:
                sequence.append('T')

    print('>seq-', i)
    print("".join(sequence))






"""
python3 rand_seq.py 3 10 20 0.5
>seq-0
GCGCGACCTTAT
>seq-1
ATCCTAGAAGT
>seq-2
CTTCGCTCGTG
"""
