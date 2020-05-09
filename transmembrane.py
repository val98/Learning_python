#!/usr/bin/env python3

import gzip
import sys
import fileinput

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

filename = sys.argv[1]
#print(filename)



def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def getKD(pep):
    total = 0
    for aa in pep:
        if aa == "I": total += 4.5
        elif aa == "V": total += 4.5
        elif aa == "L": total += 3.8
        elif aa == "F": total += 2.8
        elif aa == "C": total += 2.5
        elif aa == "M": total += 1.9
        elif aa == "A": total += 1.8
        elif aa == "G": total += -0.4
        elif aa == "T": total += -0.7
        elif aa == "S": total += -0.8
        elif aa == "W": total += -0.9
        elif aa == "Y": total += -1.3
        elif aa == "P": total += -1.6
        elif aa == "H": total += -3.2
        elif aa == "E": total += -3.5
        elif aa == "Q": total += -3.5
        elif aa == "D": total += -3.5
        elif aa == "N": total += -3.5
        elif aa == "K": total += -3.9
        elif aa == "R": total += -4.5

    return total/len(pep)



def window(seq, kd, length):
    for i in range(len(seq)-length+1):
        peptide = seq[i:i+length]
        if getKD(peptide) >= kd and 'P' not in peptide:
            return True

    return False





for name, seq in read_fasta('proteins.fasta.gz'):
    if window(seq[:30], 2.5, 8) and window(seq[30:], 2.0 , 11): print(name)




"""
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
