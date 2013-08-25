import random
import solution

def mutate(rDown,params,solSettings):
    pop = rDown[0]

    ret = []

    for p in pop:
        y = p.duplicate()
        for i in xrange(len(y.gene)):
            if random.random()<params['rate']['value']:
                if y.gene[i]==1:
                    y.gene[i]=0
                else:
                    y.gene[i] = 1
                y.gene[i] = not y.gene[i]
        ret.append(y)

    return ret

def uniRecomb(rDown,params,solSettings):
    pop = rDown[0]
    ret = []
    if not pop:
        return ret
    for i in xrange(params['num']['value']):
        y = solution.solution(solSettings)
        for j in xrange(len(y.gene)):
            y.gene[j] = random.choice(pop).gene[j]
        y.fitness = 0.0
        ret.append(y)
    
    return ret 

def diagonal(rDown,params,solSettings):
    pop = rDown[0]
    if not pop:
        return []
    childs = [solution.solution(solSettings) for p in pop]
    pnts = [random.randint(1,solSettings['settings']['length']-1) for i in xrange(params['n']['value'])]
    pnts.sort()

    pnts.append(solSettings['settings']['length'])

    for c in childs:
        last = 0
        nex = pnts[0]
        for i in xrange(1,len(pnts)+1):
            if i!=len(pnts):
                c.gene[last:nex] = pop[i%len(pop)].gene[last:nex]
                last = nex
                nex = pnts[i]
            else:
                c.gene[last:] = pop[i%len(pop)].gene[last:]
        d = pop[0]
        pop = pop[1:]
        pop.append(d)
    return childs


def evaluate(rDown,params,solSettings = {}):
    for ind in rDown[0]:
        ind.evaluate()
    return rDown[0]

def kTourn(rDown, params,solSettings):
    sel = []
    pop = rDown[0]
    if not pop:
        return []
    for n in xrange(params['count']['value']):
        best = None
        for i in xrange(params['k']['value']):
            obj = random.choice(pop)
            if not best or obj>best:
                best = obj
        sel.append(best)
    return sel


def trunc(rDown, params, solSettings):
    pop = rDown[0]
    pop.sort(reverse = True)
    return pop[:params['count']['value']]

def union(rDown, params, solSettings={}):
   right = set(rDown[0])
   left = set(rDown[1])
   return list(right.union(left))
    

