# cython: profile=True
import sys
import time
import random
import settings
import bbsa
import copy
import pareto
from mpi4py import MPI
import process manager

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank!=0:
    processManager.childProc()

else:
    proc = processManager.processManager()
    s = None
    if len(sys.argv)>1:
        s = settings.runSettings(sys.argv[1])
    else:
        s = settings.runSettings()
    s.seed =time.time()
    random.seed(s.seed)
    mu = 100 
    k = 8

    pop = []
    i = 0
    while i<mu:
        x = bbsa.bbsa(copy.deepcopy(s))
        if not x.evalExist() or not x.lastExist():
            continue
        proc.add(x)
        i+=1
    proc.start()
    proc.wait(mu)
    pop = proc.getPop()
    pop.sort()
    for p in pop:
        print p.aveBest

    maxEvals = 5000
    cur = mu
    children = 40

    fronts = pareto.pareto(pop)


    while cur<maxEvals:
        
        c = 0
        childs = []
        while c<children:    
            choice = random.choice([0,1,2])
            rate = random.random()
            
            if c+1!=children and rate<.3:
                mom = fronts.tournSelect(k)
                dad = fronts.tournSelect(k)
                x,y = mom.mate(dad)
                if x.evalExist() and x.lastExist():
                    proc.add(x)
                    c+=1
                if y.evalExist() and y.lastExist():
                    proc.add(y)
                    c+=1
            elif rate<.6:
                x=fronts.tournSelect(k).mutate()
                if x.evalExist() and x.lastExist():
                    proc.add(x)
                    c+=1
            else:
                x = fronts.tournSelect(k).altMutate()
                if x.evalExist():
                    proc.add(x)
                    c+=1
        proc.start()
        proc.wait(children)
        childs = proc.getPop()
        
        pop = fronts.getPop()
        pop.extend(childs)
        fronts = pareto.pareto(pop)
        fronts.keepMu(mu)
        cur+=children
        su = 0.0
        ave = 0.0
        for i in xrange(mu):
            su+=fronts.pop[i].aveBest
        ave = su/mu
        i = 0
        print cur, ave, len(fronts.fronts.keys())
        fronts.fronts[0].sort()
        for ind in fronts.fronts[0]: 
            print"\t",i,ind.aveBest,",",ind.aveEval,",",ind.time,",",ind.distance,"\t",ind.name
            i+=1
            ind.makeGraph()
            ind.plot()
            ind.logger.log()
            f = open(str(ind.name)+"allones.py","w")
            f.write(ind.makeProg())
            f.close()


    i = 0
    fronts.fronts[0].sort()
    for ind in fronts.fronts[0]: 
        print"\t",i,ind.aveBest,",",ind.aveEval,",",ind.time,",",ind.distance,"\t",ind.name
        i+=1
        ind.name = "finalFront/"+ind.name
        ind.logger.name = ind.name
        ind.makeGraph()
        ind.plot()
        ind.logger.log()
        f = open(str(ind.name)+"allones.py","w")
        f.write(ind.makeProg())
        f.close()

    proc.kill()





























