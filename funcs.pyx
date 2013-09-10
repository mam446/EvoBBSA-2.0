# cython: profile=True
from random import random,randrange
import solution

def mutate(rDown,params,solSettings):
    cdef int i
    pop = rDown[0]

    ret = []

    for p in pop:
        y = p.duplicate()
        for i in xrange(len(y.gene)):
            if random()<params['rate']['value']:
                if y.gene[i]==1:
                    y.gene[i]=0
                else:
                    y.gene[i] = 1
        ret.append(y)

    return ret

def uniRecomb(rDown,params,solSettings):
    cdef int i
    cdef int j
    pop = rDown[0]
    ret = []
    if not pop:
        return ret
    l= len(pop[0].gene)
    s = len(pop)
    for i in xrange(params['num']['value']):
        y = solution.solution(solSettings)
        for j in xrange(l):
            y.gene[j] = pop[randrange(0,s)].gene[j]
        y.fitness = 0.0
        ret.append(y)
    
    return ret 

def diagonal(rDown,params,solSettings):
    cdef int i,j,last,nex,p,po,l 
    pop = rDown[0]
    if not pop:
        return []
    childs = [solution.solution(solSettings) for d in pop]
    l = len(pop[0].gene)
    pnts = [randrange(1,l) for i in xrange(params['n']['value'])]
    pnts.sort()


    pnts.append(len(pop[0].gene))
    p = len(pnts)
    po = len(pop)
    for j in xrange(len(childs)):
        last = 0
        nex = pnts[0]
        g = childs[j].gene
        for i in xrange(1,p-1):
            g[last:nex] = pop[i%po].gene[last:nex]
            last = nex
            nex = pnts[i]
            
        g[last:] = pop[p%po].gene[last:]
        d = pop[0]
        pop = pop[1:]
        pop.append(d)
    return childs


def evaluate(rDown,params,solSettings = {}):
    cdef int i
    for i in xrange(len(rDown[0])):
        rDown[0][i].evaluate()
    return rDown[0]

def kTourn(rDown, params,solSettings):
    cdef int n,i
    sel = []
    pop = rDown[0]
    p = len(pop)
    if not pop:
        return []
    for n in xrange(params['count']['value']):
        best = None
        for i in xrange(params['k']['value']):
            obj = pop[randrange(0,p)]
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
    

