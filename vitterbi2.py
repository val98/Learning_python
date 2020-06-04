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
parser.add_argument('--initprob1', required=False, type=float, default=0.5,
	metavar='<float>', help='optional floating point argument [%(default)f]')
parser.add_argument('--initprob2', required=False, type=float, default=0.5,
	metavar='<float>', help='optional floating point argument [%(default)f]')

# finalization
arg = parser.parse_args()


def makeMatrix (width, height, fillSymbol):
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

	score = makeMatrix(len(seq), len(states.keys()), 0)
	final = makeMatrix(len(seq), len(states.keys()), '')
	maxScore = -1
	maxScoreX = None
	maxScoreY = None

	score = fillInitialCol(score, initialProbs)

	for j in range(1, len(score[0])): #columns
		letter = seq[j-1]
		for i in range(len(states.keys())):
			for k in range(len(states.keys())):

				#calculate probabilities
				print(j, i, k, i)
				p = score[i][j-1] * (emission[states[i]][letter])* (transition[states[k]][states[i]])

				if p > maxScore:
					maxScore = p
					maxScoreX = i
					maxScoreY = j

				score[i][j] = maxScore
				final[i][j] = maxScoreX #the row = the state

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



#states = { "CpG": arg.initprob1, "G":arg.initprob2}
states = {
			0 : 'CpG',
			1 : 'G'
		}



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
