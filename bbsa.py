import random
from funcs import *


{'Union': [{'kTourn(k=21,count=22': [{'kTourn(k=21,count=22': [{'uniRecomb(count=2)': [{'diagonal(n =24)': [{'kTourn(k=7,count=21': [{'Evaluate': [{'makeSet {A}': [{'uniRecomb(count=23)': [{'Union': ['last', {'makeSet {A}': [{'trunc(count=21': [{'kTourn(k=7,count=23': [{'kTourn(k=21,count=22': [{'kTourn(k=21,count=22': [{'uniRecomb(count=2)': [{'diagonal(n =24)': [{'kTourn(k=7,count=21': [{'Evaluate': [{'makeSet {A}': [{'uniRecomb(count=23)': [{'Union': ['last', {'Evaluate': ['last']}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'Evaluate': [{'Union': [{'diagonal(n =21)': [{'kTourn(k=19,count=6': [{'mutate(0.134211158317)': ['last']}]}]}, {'diagonal(n =8)': [{'trunc(count=23': [{'Evaluate': ['last']}]}]}]}]}]}


def run():


seed = 1377717513.5

bbsaSettings = {'runs': 5, 'maxIterations': 10000, 'maxStartNodes': 15, 'mutateMax': 5, 'maxEvals': 50000, 'initPopMax': 50, 'converge': 25, 'maxDepth': 5, 'maxOps': 5000000}

nodeSettings = {'mutate': {'rate': {'range': (0.0, 1.0), 'type': 'float', 'value': 0.0}, 'weight': 2}, 'diagonal': {'weight': 2, 'n': {'range': (1, 25), 'type': 'int', 'value': 1}}, 'makeSet': {'name': {'type': 'str', 'value': ''}, 'weight': 2}, 'uniRecomb': {'num': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'kTourn': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'k': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'trunc': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}}

solSettings = {'settings': {'length': 210}, 'prob': 'allOnes', 'weight': 1, 'repr': 'bitString'}

def run():
	A = []
	B = []
	

	last = [solution.solution(solSettings) for i in xrange(33)]

	for i in xrange(bbsaSettings['maxEvals']:
		x00000000000= last
        x00000000001000000000000= last
        x000000000010000000000010= last
        x00000000001000000000001 = Evaluate([x000000000010000000000010])
        x0000000000100000000000 = union([x00000000001000000000000,x00000000001000000000001])
        x000000000010000000000 = uniRecomb([x0000000000100000000000],{'num':23})
        A = x000000000010000000000
        x00000000001000000000=x000000000010000000000
        x0000000000100000000 = Evaluate([x00000000001000000000])
        x000000000010000000 = kTourn([x0000000000100000000],{'count':21,'k':7})
        x00000000001000000 = diagonal([x000000000010000000],{'n':24})
        x0000000000100000 = uniRecomb([x00000000001000000],{'num':2})
        x000000000010000 = kTourn([x0000000000100000],{'count':22,'k':21})
        x00000000001000 = kTourn([x000000000010000],{'count':22,'k':21})
        x0000000000100 = kTourn([x00000000001000],{'count':23,'k':7})
        x000000000010 = trunc([x0000000000100],{'count':21})
        A = x000000000010
        x00000000001=x000000000010
        x0000000000 = union([x00000000000,x00000000001])
        x000000000 = uniRecomb([x0000000000],{'num':23})
        A = x000000000
        x00000000=x000000000
        x0000000 = Evaluate([x00000000])
        x000000 = kTourn([x0000000],{'count':21,'k':7})
        x00000 = diagonal([x000000],{'n':24})
        x0000 = uniRecomb([x00000],{'num':2})
        x000 = kTourn([x0000],{'count':22,'k':21})
        x00 = kTourn([x000],{'count':22,'k':21})
        x0100000= last
        x010000 = mutate([x0100000],{'rate':0.134211158317})
        x01000 = kTourn([x010000],{'count':6,'k':19})
        x0100 = diagonal([x01000],{'n':21})
        x0101000= last
        x010100 = Evaluate([x0101000])
        x01010 = trunc([x010100],{'count':23})
        x0101 = diagonal([x01010],{'n':8})
        x010 = union([x0100,x0101])
        x01 = Evaluate([x010])
        x0 = union([x00,x01])
        last = x0

	last.extend(A)
	last.extend(B)
	for ind in last:
		ind.evaluate()
	return last

