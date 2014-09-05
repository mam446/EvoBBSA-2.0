# cython: profile=True
import sys
import time
import random
import settings
import bbsa
import copy
from mpi4py import MPI
import processManager

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
        print "here"
        x = bbsa.bbsa(copy.deepcopy(s))
        if not x.evalExist() or not x.lastExist():
            continue
        proc.add(x)
        i+=1
    print "start"
    proc.start()
    print "wait"
    proc.wait(mu)
    print "not wait"  
    pop = proc.getPop()    
    pop.sort()
    for p in pop:
        print p.aveBest

    maxEvals = 5000
    cur = mu
    children = 40

    while cur<maxEvals:
        
        c = 0
        childs = []
        while c<children:    
            choice = random.choice([0,1,2])
            rate = random.random()
            
            if c+1!=children and rate<.3:
                mom = ktourn(pop,k)
                dad = ktourn(pop,k)
                x,y = mom.mate(dad)
                if x.evalExist() and x.lastExist():
                    proc.add(x)
                    c+=1
                if y.evalExist() and y.lastExist():
                    proc.add(y)
                    c+=1
            elif rate<.6:
                x=ktourn(pop,k).mutate()
                if x.evalExist() and x.lastExist():
                    proc.add(x)
                    c+=1
            else:
                x = ktourn(pop,k).altMutate()
                if x.evalExist():
                    proc.add(x)
                    c+=1
        print "start"
        proc.start()
        print "wait"
        proc.wait(children)
        print "no wait"
        childs = proc.getPop()
        pop.extend(childs)
        pop.sort()
        pop.reverse()
        pop = pop[:mu]
        cur+=children

        su = 0.0
        ave = 0.0
        for i in xrange(len(pop)):
            su+=pop[i].aveBest
        ave = su/len(pop)
        
        print cur, ave,pop[0].aveBest,pop[0].aveEval,pop[0].aveOps
        pop[0].makeGraph()
        pop[0].plot()
        pop[0].logger.log()
        f = open(str(pop[0].name)+"allones.py","w")
        f.write(pop[0].makeProg())
        f.close()
    print
    print pop[0].aveBest,pop[0].aveEval
    print pop[0].toDict()
    f = open(str(pop[0].name)+"-Dumb.py","w")
    f.write(pop[0].makeProg())
    f.close()

    proc.kill()






























