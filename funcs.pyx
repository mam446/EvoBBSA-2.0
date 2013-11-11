# cython: profile=True
from random import random,randrange,gauss,choice
import solution
import math
def mutate(rDown,params):
    cdef int i
    pop = rDown[0]

    ret = []
    l = 0
    if pop:
        l = len(pop[0].gene)

    for p in pop:
        y = p.duplicate()
        for i in xrange(l):
            if random()<params['rate']['value']:
                if y.gene[i]==1:
                    y.gene[i]=0
                else:
                    y.gene[i] = 1
        ret.append(y)

    return ret

def gaussian(rDown,params):
    pop = rDown[0]

    ret = []
    
    l = 0
    if pop:
        l=len(pop[0].gene)

    for p in pop:
        y = p.duplicate()
        for i in xrange(l):
            if random()<params['rate']['value']:
                y.gene[i]+=gauss(0,math.sqrt(params['variance']['value']))
        ret.append(y)
    return ret




def uniRecomb(rDown,params):
    cdef int i
    cdef int j
    pop = rDown[0]
    ret = []
    if not pop:
        return ret
    l= len(pop[0].gene)
    s = len(pop)
    for i in xrange(params['num']['value']):
        y = pop[0].duplicate()
        for j in xrange(l):
            y.gene[j] = pop[randrange(0,s)].gene[j]
        y.fitness = 0.0
        ret.append(y)
    
    return ret 

def uniRecomb2(rDown,params):
    cdef int i
    cdef int j
    left = None
    right = None
    if rDown[0]:
        left = rDown[0][0]
    if  len(rDown[1])>1:
        right = rDown[1][0]
    if not right:
        if not left:
            return []
        else:
            return [left]


    l= len(right.gene)
    
    y = right.duplicate()
    x = left.duplicate()
    for j in xrange(l):
        if random.choice([0,1]):
            y.gene[j] = right.gene[j]
            x.gene[j] = left.gene[j]
        else:
            y.gene[j] = left.gene[j]
            x.gene[j] = right.gene[j]
    y.fitness = 0.0
    x.fitness = 0.0
    
    ret = [x,y]
    return ret 




def onePoint(rDown,params={}):
    if not rDown[0]:
        return rDown[1]
    if not rDown[1]:
        return rDown[0]

    right = rDown[0][0].duplicate()
    left = rDown[1][0].duplicate()

    
    p = randrange(0,len(right.gene))

    rTemp = left.gene[p:]
    left.gene[p:] = right.gene[p:]
    right.gene[p:] = rTemp
    return [right,left]

def diagonal(rDown,params):
    cdef int i,j,last,nex,p,po,l 
    pop = rDown[0]
    if not pop:
        return []
    childs = [d.duplicate() for d in pop]
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


def evaluate(rDown,params={}):
    cdef int i
    for i in xrange(len(rDown[0])):
        rDown[0][i].evaluate()
        params['state'].bestSoFar(rDown[0][i])
        params['state'].curEval+=1

    return rDown[0]

def kTourn(rDown, params):
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


def trunc(rDown, params):
    pop = rDown[0]
    pop.sort(reverse = True)
    return pop[:params['count']['value']]

def union(rDown, params={}):
   right = set(rDown[0])
   left = set(rDown[1])
   return list(right.union(left))
    
def randSubset(rDown,params):
    cdef int i,p
    down = rDown[0]
    if not down:
        return []
    ret = []
    p = len(down)
    for i in xrange(params['count']['value']):
        ret.append(down[randrange(0,p)])
    return ret
    










