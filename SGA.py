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


s = None
if len(sys.argv)>1:
    s = settings.runSettings(sys.argv[1])
else:
    s = settings.runSettings()
s.seed =time.time()
random.seed(s.seed)
mu = 50 
k = 8

pop = []
i = 0
while i<mu:
    x = bbsa.bbsa(copy.deepcopy(s))
    if not x.evalExist() or not x.lastExist():
        print "\nFailed\n"
        continue
    print x.toDict()
    x.evaluate()
    if x.valid():
        pop.append(x)
        print "------------------------------------------------------",x.aveBest
        print "--------------------------------------------",x.aveEval
        i+=1
    else:
        print "################################################################"
pop.sort()
for p in pop:
    print p.aveBest

maxEvals = 2000
cur = mu
children = 20

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
                x.evaluate()
                childs.append(x)
                c+=1
            if y.evalExist() and y.lastExist():
                y.evaluate()
                childs.append(y)
                c+=1
        elif rate<.6:
            x=ktourn(pop,k).mutate()
            if x.evalExist() and x.lastExist():
                x.evaluate()
                childs.append(x)
                c+=1
        else:
            x = ktourn(pop,k).altMutate()
            if x.evalExist():
                x.evaluate()
                childs.append(x)
                c+=1

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































