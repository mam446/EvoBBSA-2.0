# cython: profile=True
import sys
import time
import random
import settings
import bbsa
import copy
import pareto
from mpi4py import MPI
import processManager

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best


def runMpiSGA(settingsFile = None):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()


    if rank!=0:
        processManager.childProc()

    else:
        proc = processManager.processManager()
        s = None
        if not settingsFile:
            if len(sys.argv)<2:
                raise "Must suply settings file"
            settingsFile = sys.argv[1]
        s = settings.runSettings(settingsFile) 
        
        if s.hyperSettings['seed']:
            s.seed = s.hyperSEttings['seed']
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
            proc.add(x)
            i+=1
        proc.start()
        proc.wait(mu)
        pop = proc.getPop()
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
                        proc.add(x)
                        c+=1
                    if y.evalExist() and y.lastExist():
                        proc.add(y)
                        c+=1
                elif rate<mateRate+mutateRate:
                    x=fronts.tournSelect(childK).mutate()
                    if x.evalExist() and x.lastExist():
                        proc.add(x)
                        c+=1
                else:
                    x = fronts.tournSelect(childK).altMutate()
                    if x.evalExist():
                        proc.add(x)
                        c+=1
            proc.start()
            proc.wait(lamb)
            childs = proc.getPop()
            
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
                f = open(str(ind.name)+"allones.py","w")
                f.write(ind.makeProg())
                f.close()


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
            f = open(str(ind.name)+"allones.py","w")
            f.write(ind.makeProg())
            f.close()

        proc.kill()






if __name__ =="__main__":
    runMpiSGA()






















