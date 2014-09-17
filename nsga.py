# cython: profile=True
import sys
import time
import random
import settings
import bbsa
import copy
import pareto

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best

def runNSGA(settingsFile = None):

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
        else:
    pop.sort()
    for p in pop:
        print p.fitness


    fronts = pareto.pareto(pop)


    while cur<maxEvals:
        
        c = 0
        childs = []
        while c<lamb:    
            choice = random.choice([0,1,2])
            rate = random.random()
            
            if c+1!=lamb and rate<mateRate:
                mom = fronts.tournSelect(childK)
                dad = fronts.tournSelect(childK)
                x,y = mom.mate(dad)
                if x.evalExist() and x.lastExist():
                    x.evaluate()
                    if x.aveEval>0:
                        childs.append(x)
                        c+=1
                if y.evalExist() and y.lastExist():
                    y.evaluate()
                    if y.aveEval>0:
                        childs.append(y)
                        c+=1
            elif rate<mateRate+mutateRate:
                x=fronts.tournSelect(childK).mutate()
                if x.evalExist() and x.lastExist():
                    x.evaluate()
                    if x.aveEval>0:
                        childs.append(x)
                        c+=1
            else:
                x = fronts.tournSelect(childK).altMutate()
                if x.evalExist():
                    x.evaluate()
                    if x.aveEval>0:
                        childs.append(x)
                        c+=1
        pop = fronts.getPop()
        pop.extend(childs)
        fronts = pareto.pareto(pop)
        fronts.keepMu(mu)
        cur+=lamb
        su = 0.0
        ave = 0.0
        for i in xrange(mu):
            su+=fronts.pop[i].fitness
        ave = su/mu
        i = 0
        print cur, ave, len(fronts.fronts.keys())
        fronts.fronts[0].sort()
        for ind in fronts.fronts[0]: 
            print"\t",i,ind.fitness,",",ind.aveEval,",",ind.time,",",ind.distance,"\t",ind.name
            i+=1
            ind.makeGraph()
            ind.plot()
            ind.logger.log()
            ind.makeProg()


    i = 0
    fronts.fronts[0].sort()
    for ind in fronts.fronts[0]: 
        print"\t",i,ind.fitness,",",ind.aveEval,",",ind.time,",",ind.distance,"\t",ind.name
        i+=1
        ind.name = "finalFront/"+ind.name
        ind.logger.name = ind.name
        ind.makeGraph()
        ind.plot()
        ind.logger.log()
        ind.makeProg()


if __name__ =="__main__":
    runNSGA()




























