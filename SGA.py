# cython: profile=True
import sys
import time
import random
import settings
import bbsa
import copy

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best

def runSGA(settingsFile = None):
    s = None
    if not settingsFile:
        if len(sys.argv)<2:
            raise "Must supply settings file"
        settingsFile = sys.argv[1] 
    s = settings.runSettings(settingsFile,sys.argv[2])

    if s.hyperSettings['seed']:
        s.seed = s.hyperSettings['seed']
    else:
        s.seed =time.time()
    random.seed(s.seed)
    
    
    mu = s.hyperSettings['mu'] 
    childK = s.hyperSettings['childK']
    lamb = s.hyperSettings['lambda']
    maxEvals = s.hyperSettings['evaluations']
    
    mutateRate = s.hyperSettings['mutateRate']
    mateRate = s.hyperSettings['mateRate']
    
    cur = mu
    pop = []


    i = 0
    while i<mu:
        x = bbsa.bbsa(copy.deepcopy(s))
        if not x.evalExist() or not x.lastExist():
            continue
        x.evaluate()
        if x.valid():
            pop.append(x)
            i+=1
    
    pop.sort()
    for p in pop:
        print p.fitness


    while cur<maxEvals:
        
        c = 0
        childs = []
        while c<lamb:    
            choice = random.choice([0,1,2])
            rate = random.random()
            
            if c+1!=lamb and rate<mateRate:
                mom = ktourn(pop,childK)
                dad = ktourn(pop,childK)
                x,y = mom.mate(dad)
                if x.evalExist() and x.lastExist():
                    x.evaluate()
                    childs.append(x)
                    c+=1
                if y.evalExist() and y.lastExist():
                    y.evaluate()
                    childs.append(y)
                    c+=1
            elif rate<mateRate+mutateRate:
                x=ktourn(pop,childK).mutate()
                if x.evalExist() and x.lastExist():
                    x.evaluate()
                    childs.append(x)
                    c+=1
            else:
                x = ktourn(pop,childK).altMutate()
                if x.evalExist():
                    x.evaluate()
                    childs.append(x)
                    c+=1

        pop.extend(childs)
        pop.sort()
        pop.reverse()
        pop = pop[:mu]
        cur+=lamb

        su = 0.0
        ave = 0.0
        for i in xrange(len(pop)):
            su+=pop[i].fitness
        ave = su/len(pop)
        
        print cur, ave,pop[0].fitness,pop[0].aveEval,pop[0].aveOps
        pop[0].makeGraph()
        pop[0].plot()
        pop[0].logger.log()
        
        pop[0].makeProg()
        f.close()
    print
    print pop[0].fitness,pop[0].aveEval
    print pop[0].toDict()
    f = open(str(pop[0].name)+"-Dumb.py","w")
    pop[0].makeProg()
    f.close()


if __name__ =="__main__":
    runSGA()




























