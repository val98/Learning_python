#!/usr/bin/env python3

# sequence, subsequence, window,

import biotools as bt
import argparse
import fileinput

parser = argparse.ArgumentParser(
	description='Computes hydrophobicity of given protein sequence.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='fasta file name to get sequence from')
parser.add_argument('--initprobCpG', required=False, type=float, default=0.6,
	metavar='<float>', help='optional floating point argument [%(default)f]')
parser.add_argument('--initprobG', required=False, type=float, default=0.4,
	metavar='<float>', help='optional floating point argument [%(default)f]')

# finalization
arg = parser.parse_args()


def makeMatrix (width, height, fillSymbol):
	#matrix = [fillSymbol] * width
	matrix = []
	for i in range(height):
		matrix.append([fillSymbol]*(width+1))

	return matrix

def printMatrix(matrix, topSeq, states):
	listSeq = topSeq.split()
	print(' 	', "       ".join(topSeq))
	i = 0

	for i in range(len(states)):
		print(states[i], matrix[i])

	return

def fillInitialCol(matrix, initialProbs):
	for i in range(len(matrix)):
		matrix[i][0] = initialProbs[i]

	return matrix

def vitterbi(seq, states, initialProbs):

	score = makeMatrix(len(seq), len(states), 0)
	final = makeMatrix(len(seq), len(states), '')
	maxScore = 0
	maxScoreX = None
	maxScoreY = None

	score = fillInitialCol(score, initialProbs)
	#score[0][0] = states['CpG']
	#score[1][0] = states['G']

	#make the matrix of probabilities

	#prevMax = max(score[0][0], score[1][0])
	#maxScoreX = 0
	#maxScoreY = 0
	i = 0
	for j in range(1, len(score[0])): #columns
		#calculate probabilities
		letter = seq[j-1]
		a = score[i][j-1] * (emission['CpG'][letter])* (transition['CpG']['CpG'])
		c = score[i+1][j-1] * (emission['CpG'][letter])* (transition['G']['CpG'])

		b = score[i][j-1] * (emission['G'][letter])* (transition['CpG']['G'])
		d = score[i+1][j-1] * (emission['G'][letter])* (transition['G']['G'])

		#fill in traceback
		if a > c: # came from CpG, stayed in CpG
			prevMaxCpG = a
			final[i][j] = 0
		else: #c > a:  came from G, transition to CpG
			prevMaxCpG = c
			final[i][j] = 1

		if b > d: # came from CpG, transition to G
			prevMaxG = b
			final[i+1][j] = 0
		else:  #d > b: # came from G, stayed in G
			prevMaxG = d
			final[i+1][j] = 1

		score[i][j] = prevMaxCpG
		score[i+1][j] = prevMaxG


		#outside of inner loop --> find max, set new preMax

	print('score Matrix: ')
	printMatrix(score, seq, states )
	print('final matrix: ')
	printMatrix(final, seq, states )
	list = []

	if score[0][len(seq)] > score[1][len(seq)]:
		maxState = 0 #maxState = CpG or G
		list.append(maxState)
	else:
		maxState = 1
		list.append(maxState)

	for i in range(len(seq)-1, 0, -1):
		gotoState = final[maxState][i]
		list.append(gotoState)
		maxState = gotoState


	for n in range(len(list)):
		if list[n] == 0:
			list[n] = 'CpG'
		if list[n] == 1:
			list[n] = 'G'
	print('list: ', list)

	return list

emission = {
			'CpG':{'A': 0.1, 'C':0.4, 'G':0.4, 'T':0.1},
			'G':{'A':0.25, 'C':0.25, 'G':0.25, 'T':0.25}
        }
transition ={
			'CpG':{'CpG': 0.7, 'G':0.3},
			'G':{'CpG':0.3, 'G':0.7}
			}


states = ["CpG", "G"]
#states = { "CpG": arg.initprob1, "G":arg.initprob2}
"""
states = {
			"CpG" :0,
			"G" : 1
		}
"""


initialProbs = [0.6, 0.4]

for line in fileinput.input(arg.file):
    if line[0] == '#':
        continue
    else:
        line = line.rstrip()
        print(line)

list = []
list = vitterbi(line, states, initialProbs)
print('-'.join(list[::-1]))
