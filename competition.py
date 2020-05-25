#!/usr/bin/env python3

# Modify entropy_fast() however you like to make it faster
# Ideally, your method is faster at all ranges of window size

import math
import time
import random

def entropy_slow(seq, w, th):
	t0 = time.perf_counter()
	low_H_count = 0

	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		a, c, g, t = 0, 0, 0, 0
		for nt in win:
			if   nt == 'A': a += 1
			elif nt == 'C': c += 1
			elif nt == 'G': g += 1
			elif nt == 'T': t += 1

		total = a + c + g + t
		h = 0
		pa, pc, pg, pt = a/total, c/total, g/total, t/total


		if a != 0: h -= pa * math.log2(pa)
		if c != 0: h -= pc * math.log2(pc)
		if g != 0: h -= pg * math.log2(pg)
		if t != 0: h -= pt * math.log2(pt)

		if h < th: low_H_count += 1


	t1 = time.perf_counter()

	return low_H_count, t1-t0

def entropy_fast(seq, w, t):

	t0 = time.perf_counter()
	low_H_count = 0

	for i in range(len(seq) - w + 1):
		win = seq[i:i+w]
		nucleotides = {"A":0, "C":0, "G":0, "T":0}
		#a, c, g, t = 0, 0, 0, 0
		for nt in win:
			nucleotides[nt] +=1
			#print(nucleotides)
			#if   nt == 'A': a += 1
			#elif nt == 'C': c += 1
			#elif nt == 'G': g += 1
			#elif nt == 'T': t += 1
		#total = a + c + g + t
		total = nucleotides["A"] + nucleotides["C"] + nucleotides["G"] + nucleotides["T"]
		h = 0
		pa, pc, pg, pt = nucleotides["A"]/total, nucleotides["C"]/total, nucleotides["G"]/total, nucleotides["T"]/total

		if nucleotides["A"] != 0: h -= pa * math.log2(pa)
		if nucleotides["C"] != 0: h -= pc * math.log2(pc)
		if nucleotides["G"] != 0: h -= pg * math.log2(pg)
		if nucleotides["T"] != 0: h -= pt * math.log2(pt)

		if h < t: low_H_count += 1

	t1 = time.perf_counter()
	#print("fast h: ", h)
	#print("fast low H-count", low_H_count)
	return low_H_count, t1-t0

# create a random chromosome
seq = []
alph = ['A', 'C', 'G', 'T']
for i in range(int(1e5)):
	seq.append(alph[random.randint(0,3)])
seq = ''.join(seq)

"""
dna = "ATTACCGTAATCTAC"
cs, ts = entropy_slow(dna, 15, 1)
cf, tf = entropy_fast(dna, 15, 1)
print("Cs, ts:",cs, ts)
print("Cf, tf:", cf, tf)

# test speed at various word sizes
"""
W = [7, 15, 100]
for w in W:
	cs, ts = entropy_slow(seq, w, 1)
	cf, tf = entropy_fast(seq, w, 1)
	assert(cs == cf)
	print("width:", w,"  ", tf / ts)
