import random
from funcs import *


{'trunc(count=24': [{'makeSet {A}': [{'Union': ['last', {'Evaluate': [{'Union': [{'Union': [{'diagonal(n =10)': ['A']}, {'uniRecomb(count=9)': ['last']}]}, {'mutate(0.982775243811)': ['last']}]}]}]}]}]}


evals = 50860.0

ops = 182924.045455

fit = 0.944047619048

seed = 1378698184.16

bbsaSettings = {'runs': 5, 'maxIterations': 10000, 'maxStartNodes': 15, 'mutateMax': 5, 'maxEvals': 50000, 'initPopMax': 50, 'converge': 25, 'maxDepth': 5, 'maxOps': 5000000}

nodeSettings = {'mutate': {'rate': {'range': (0.0, 1.0), 'type': 'float', 'value': 0.0}, 'weight': 2}, 'diagonal': {'weight': 2, 'n': {'range': (1, 25), 'type': 'int', 'value': 1}}, 'makeSet': {'name': {'type': 'str', 'value': ''}, 'weight': 2}, 'uniRecomb': {'num': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'kTourn': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'k': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'trunc': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}}

solSettings = {'prob': 'dTrap', 'repr': 'bitString', 'weight': 1, 'settings': {'length': 100, 'k': 5}}

def run():
	A = []
	C = []
	B = []
	

	last = [solution.solution(solSettings) for i in xrange(5)]

	for i in xrange(bbsaSettings['maxEvals']:
		x0000= last
        x00010000= A
        x0001000 = diagonal([x00010000],{'n':10})
        x00010010= last
        x0001001 = uniRecomb([x00010010],{'num':9})
        x000100 = union([x0001000,x0001001])
        x0001010= last
        x000101 = mutate([x0001010],{'rate':0.982775243811})
        x00010 = union([x000100,x000101])
        x0001 = Evaluate([x00010])
        x000 = union([x0000,x0001])
        A = x000
        x00=x000
        x0 = trunc([x00],{'count':24})
        last = x0

	last.extend(A)
	last.extend(C)
	last.extend(B)
	for ind in last:
		ind.evaluate()
	return last

