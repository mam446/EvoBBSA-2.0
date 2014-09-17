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

def runMpiNSGA(settingsFile = None):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()


    if rank!=0:
        processManager.childProc()

    else:
        proc = processManager.processManager()
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
            proc.add(x)
            i+=1
        #print "start"
        proc.start()
        #print "wait"
        proc.wait(mu)
        #print "not wait"  
        pop = proc.getPop()    
        pop.sort()
        for p in pop:
            print p.fitness


        while cur<maxEvals:
            
            c = 0
            childs = []
            while c<lamb:    
                choice = random.choice([0,1,2])
                rate = random.random()
                
                if c+1!=lamb and rate<.3:
                    mom = ktourn(pop,childK)
                    dad = ktourn(pop,childK)
                    x,y = mom.mate(dad)
                    if x.evalExist() and x.lastExist():
                        proc.add(x)
                        c+=1
                    if y.evalExist() and y.lastExist():
                        proc.add(y)
                        c+=1
                elif rate<.6:
                    x=ktourn(pop,childK).mutate()
                    if x.evalExist() and x.lastExist():
                        proc.add(x)
                        c+=1
                else:
                    x = ktourn(pop,childK).altMutate()
                    if x.evalExist():
                        proc.add(x)
                        c+=1
            #print "start"
            proc.start()
            #print "wait"
            proc.wait(lamb)
            #print "no wait"
            childs = proc.getPop()
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
        print
        print pop[0].fitness,pop[0].aveEval
        print pop[0].toDict()
        pop[0].makeProg()

        proc.kill()






if __name__=="__main__":
    runMpiNSGA()























