
from mpi4py import MPI
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

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None


if rank == 0:
    p = pareto.pareto()
    data = comm.gather(data,root=0)
    print data
    while data:
        for i in xrange(len(data)):
            
            if data[i]:
                p.push(data[i])
        data = None
        print "num",p.numFronts,len(p.top['data'])
        for i in xrange(len(p.top['data'])):
            f = open("multi"+str(i)+".py","w")
            f.write(p.top['data'][i].makeProg())
            f.close()


        data = comm.gather(data,root=0) 
        print "I got data"  
    print "root ended"
else:

    s = settings.settings()
    s.runs = 10 
    mu = 30
    k = 10

    pop = []
    i = 0
    while i<mu:
        x = bbsa.bbsa(copy.deepcopy(s))
        x.run()
        if x.aveBest!=0.0:
            pop.append(x)
            i+=1
    pop.sort()

    for x in pop:
        print x.aveBest

    maxEvals = 10000
    cur = 0
    children = 15

    while cur<maxEvals:
        
        c = 0
        childs = []
        while c<children:    
            choice = random.choice([0,1,2])
            if c+1!=children and 1==choice:
                mom = ktourn(pop,k)
                dad = ktourn(pop,k)
                x,y = mom.mate(dad)
                x.run()
                y.run()
                childs.append(x)
                childs.append(y)
                c+=2
            elif choice==2:
                x=ktourn(pop,k).mutate()
                x.run()
                childs.append(x)
                c+=1
            else:
                x = ktourn(pop,k).altMutate()
                x.run()
                childs.append(x)
                c+=1

        pop.extend(childs)
        pop.sort()
        pop.reverse()
        pop = pop[:mu]
        cur+=children
        t = pop[0].duplicate()
        t.aveBest = pop[0].aveBest
        t.aveEval = pop[0].aveEval 
        data = comm.gather(t,root=0)
        print rank,cur, pop[0].aveBest,pop[0].aveEval,pop[0].aveOps
        f = open("rank"+str(rank)+".py","w")
        f.write(pop[0].makeProg())
        f.close()

    print
    print pop[0].aveBest,pop[0].aveEval
    print pop[0].toDict()































