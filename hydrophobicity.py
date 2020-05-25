#!/usr/bin/env python3
import argparse
import biotools
# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

parser = argparse.ArgumentParser(
	description='Computes hydrophobicity of given protein sequence.')
# required arguments
parser.add_argument('--input', required=True, type=str,
	metavar='<path>', help='fasta file name to get protein sequence from')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='window size')
parser.add_argument('--method', required=True, type=str,
	metavar='<str>', help='method to calculate hydrophobicity')

# finalization
arg = parser.parse_args()

assert(arg.method == "KD" or arg.method == "IS" or arg.method == "OS" or arg.method == "ISOS")

scale = dict()

KDscale = {
           "I": 4.5, "V": 4.5, "L": 3.8, "F": 2.8, "C": 2.5,
           "M": 1.9, "A": 1.8, "G":-0.4, "T":-0.7, "S":-0.8,
           "W":-0.9, "Y":-1.3, "P":-1.6, "H":-3.2, "E":-3.5,
           "Q":-3.5, "D":-3.5, "N":-3.5, "K":-3.9, "R":-4.5
           }

ISscale = {
           "I":-0.31, "V": 0.07, "L":-0.56, "F":-1.13, "C":-0.24,
           "M":-0.23, "A": 0.17, "G": 0.01, "T": 0.14, "S": 0.13,
           "W":-1.85, "Y":-0.94, "P": 0.45, "H": 0.17, "E": 2.02,
           "Q": 0.58, "D": 1.23, "N": 0.42, "K": 0.99, "R": 0.815
           }

OSscale = {
            "I":-1.12, "V":-0.46, "L":-1.25, "F":-1.71, "C":-0.02,
            "M":-0.67, "A": 0.50, "G": 1.15, "T": 0.25, "S": 0.46,
			"W":-2.09, "Y":-0.71, "P": 0.14, "H": 0.11, "E": 3.63,
			"Q": 0.77, "D": 3.64, "N": 0.85, "K": 2.80, "R": 1.81
            }

ISOSscale = {
            "I":-0.81, "V":-0.53, "L":-0.69, "F":-0.58, "C": 0.22,
            "M":-0.44, "A": 0.33, "G": 1.14, "T": 0.11, "S": 0.33,
            "W":-0.24, "Y": 0.23, "P":-0.31, "H":-0.06, "E": 1.61,
            "Q": 0.19, "D": 2.41, "N": 0.43, "K": 1.81, "R": 1.00
            }

#scale["KD"] = dict()
scale["KD"] = KDscale
scale["IS"] = ISscale
scale["OS"] = OSscale
scale["ISOS"] = ISOSscale


def getHP(subseq, method):
    total = 0
    for AA in subseq:
        if AA in method:
        	total += method[AA]
    return total/len(subseq)



for name, seq in biotools.read_fasta(arg.input):
	print(">",name)
	hydrophobicity = 0
	for i in range(len(seq)-arg.window):
		subseq = seq[i:i+arg.window]
		hydrophobicity = getHP(subseq, scale[arg.method])
		#print("\t", subseq, hydrophobicity)
		tab = "\t"
		print('%s %s %.3f' % (tab, subseq, hydrophobicity))



    #print(name, len(seq))



"""
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""
