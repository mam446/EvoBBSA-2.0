import random
from funcs import *
import state


{'mutate(0.0172107863283)': [{'uniRecomb(count=20)': [{'trunc(count=8': [{'onePoint': [{'kTourn(k=25,count=1': [{'Evaluate': ['last']}]}, {'trunc(count=8': [{'Evaluate': [{'uniRecomb(count=15)': [{'trunc(count=19': [{'onePoint': [{'kTourn(k=25,count=1': [{'Evaluate': [{'uniRecomb(count=18)': [{'trunc(count=19': ['A']}]}]}]}, {'trunc(count=19': [{'Evaluate': [{'makeSet {A}': [{'diagonal(n =2)': ['last']}]}]}]}]}]}]}]}]}]}]}]}]}


evals = 5505.7

ops = 20164.7891963

fit = 0.850095238095

seed = 1382501921.05

bbsaSettings = {'runs': 5, 'maxIterations': 10000, 'maxStartNodes': 15, 'mutateMax': 5, 'maxEvals': 50000, 'initPopMax': 50, 'converge': 25, 'maxDepth': 5, 'probType': 'bitString', 'maxOps': 5000000}

nodeSettings = {'mutate': {'rate': {'range': (0.0, 1.0), 'type': 'float', 'value': 0.0}, 'weight': 2}, 'randSubset': {'count': {'range': (1, 25), 'type': 'int', 'value': 20}, 'weight': 2}, 'forLoop': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'onePoint': {'weight': 2}, 'diagonal': {'weight': 2, 'n': {'range': (1, 25), 'type': 'int', 'value': 1}}, 'makeSet': {'name': {'type': 'str', 'value': 'A'}, 'weight': 2}, 'uniRecomb': {'num': {'range': (1, 25), 'type': 'int', 'value': 1}, 'weight': 2}, 'kTourn': {'count': {'range': (1, 25), 'type': 'int', 'value': 1}, 'k': {'range': (1, 25), 'type': 'int', 'value': 25}, 'weight': 2}, 'trunc': {'count': {'range': (1, 25), 'type': 'int', 'value': 8}, 'weight': 2}}

solSettings = {'repr': 'bitString', 'prob': 'dTrap', 'weight': 1, 'settings': {'length': 100, 'k': 5}}

def run(numRuns,log,sol=solSettings,name = '',progConf =None):
    for i in xrange(numRuns):
        A = []
        evals = 0
        mu = 50
        lamb = 20
        k = 15
        survive = 20
        last = [solution.solution(sol) for j in xrange(mu)]

        bestLog =state.state()
        while evals< bbsaSettings['maxEvals']:
            children =[]
            for x in xrange(lamb):
                parents = kTourn([last],{'count':{'value':2},'k':{'value':k}})
                new = mutate([uniRecomb([parents],{'num':{'value':1}})],{'rate':{'value':.01}})
                children.extend(evaluate([new],{'state':bestLog}))
                evals+=len(new)
            last = kTourn([children],{'count':{'value':mu},'k':{'value':survive}})

            st = state.state()
            st.last = last
            st.curEval = evals
            log.nextIter(st)
        for ind in last:
            ind.evaluate()
        st = state.state()
        st.last = last
        st.curEval = evals
        log.nextIter(st)
        print i
        log.nextRun()
        bestLog.logBestSoFar(i,name,progConf)
        bestLog.reset()
    log.nextProbConf()
    return log
