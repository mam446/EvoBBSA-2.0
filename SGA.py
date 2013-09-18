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
    print x.toDict()
    if not x.evalExist():
        print "What"
        continue
    x.evaluate()
    if x.valid():
        pop.append(x)
        print "------------------------------------------------------",x.aveBest
        print "--------------------------------------------",x.aveOps
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
        if c+1!=children and 1==choice:
            mom = ktourn(pop,k)
            dad = ktourn(pop,k)
            x,y = mom.mate(dad)
            if x.evalExist():
                x.evaluate()
                childs.append(x)
                c+=1
            if y.evalExist():
                y.evaluate()
                childs.append(y)
                c+=1
        elif choice==2:
            x=ktourn(pop,k).mutate()
            if x.evalExist():
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
    
    f = open(str(pop[0].name)+"allones.py","w")
    f.write(pop[0].makeProg())
    f.close()
print
print pop[0].aveBest,pop[0].aveEval
print pop[0].toDict()
f = open(str(pop[0].name)+"-Dumb.py","w")
f.write(pop[0].makeProg())
f.close()































