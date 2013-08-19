import random
import solution

def mutate(rDown,params,solSettings):
    pop = rDown[0]

    ret = []

    for p in pop:
        y = p.duplicate()
        for i in xrange(len(y.bits)):
            if random.random<params['rate']['value']:
                y.bits[i] = not y.bits[i]
        ret.append(y)

    return ret

def uniRecomb(rDown,params,solSettings):
    pop = rDown[0]
    ret = []

    for i in xrange(params['count']['value']):
        y = solution.solution(solSettings)
        for j in xrange(len(y.bits)):
            y.bits[j] = random.choice(pop).bits[j]
        ret.append(y)
    
    return ret 

def diagonal(rDown,params,solSettings):
    pop = rDown[0]
    if not pop:
        return []
    childs = [solution.solution(solSettings) for p in pop]
    pnts = [random.randint(1,solSettings['length']-1) for i in xrange(params['n'])]
    pnts.sort()

    pnts.append(solSettings['length'])

    for c in childs:
        last = 0
        nex = pnts[0]
        for i in xrange(1,len(pnts)+1):
            if i!=len(pnts):
                c.bits[last:nex] = pop[i%len(pop)].bits[last:nex]
                last = nex
                nex = pnts[i]
            else:
                c.bits[last:] = pop[i%len(pop)].bits[last:]
        d = pop[0]
        pop = pop[1:]
        pop.append(d)
    return childs


def evaluate(rDown,params,solSettings):
    for ind in rDown[0]:
        ind.evaluate()

def kTourn(rDown, params,solSettings):
    sel = []
    pop = rDown[0]
    for n in xrange(params['count']):
        best = None
        for i in xrange(params['k']):
            obj = random.choice(pop)
            if not best or obj>best:
                best = obj
        sel.append(best)

    return sel


def trunc(rDown, params, solSettings):
    pop = rDown[0]
    pop.sort(reverse = True)
    return pop[:params['count']['value']]

def union(rDown, params, solSettings):
   right = set(rDown[0])
   left = set(rDown[1])
   return right.union(left)
    

