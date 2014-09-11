import re
import math
import FitnessFunction
import random
import copy
from collections import defaultdict 
#cython: profile=True
data = {}

class allOnes:
    def __init__(self,settings):
        self.settings = settings
        #this is how you store auxiliarly data that everyone can use 
        if settings['name'] not in data:
            data[settings['name']] = [1,2,3,4,5]
    def evaluate(self,gene):
        fit = 0.0
        for bit in gene:
            if bit==1:
                fit+=1.0
        return fit/len(gene)

class lsat:
    def __init__(self,settings):
        self.settings =settings

        if settings['name'] not in data:
            data[settings['name']] = self.loadEquation(settings['name'])
        

    def evaluate(self,gene):
        return self.evalEquation(data[self.settings['name']],gene)/float(len(data[self.settings['name']]))

    def loadEquation(self,filename):
        f = open(filename)
        
        probType =None
        variables = None
        clauses = None

        comment = True
        cur = None
        while comment:
            cur = f.readline()
            if cur[0] != 'c':
                break
        if cur[0]=='p':
            data = re.split('\W+',cur)
            print data
            #data = cur.split(' ')
            probType = data[1]
            variables = int(data[2])
            clauses = int(data[3])

        eq = []

        for i in xrange(clauses):
            cur = f.readline()
            eq.append(map(int,re.split('\W+',cur)[:-1]))
        
        return eq 
    
    
    def generateEquation(self,termNum,clauseNum):
        eq = [[random.choice([-1,1])*random.randint(1,termNum)for j in xrange(self.settings['L'])]for i in xrange(clauseNum)]


        return eq

    def evalEquation(self,eq,bits):
        num = 0
        cdef int i,y
        for i in xrange(len(eq)):
            check = False
            for y in eq[i]:
                if y>0:
                    
                    if bits[y-1]==1:
                        check = True
                        break
                else:
                    if bits[-y-1]==0:
                        check = True
                        break
            if check:
                num+=1
        return num
        
    def SAWStats(self,bits,sawHistory = None):
        eq = data[self.settings['name']]
        cdef int i,y
        if sawHistory==None:
            sawHistory = [0]*len(eq)
        for i in xrange(len(eq)):
            check = False
            for y in eq[i]:
                if y>0:
     
                    if bits[y-1]==1:
                        check = True
                        break
                else:
                    if bits[-y-1]==0:
                        check = True
                        break
            if check:
                sawHistory[i] = 0
            else:
                sawHistory[i] += 1
        return sawHistory

    def SAWMutate(self,bits,sawHistory):
        eq = data[self.settings['name']]
        cdef int i,mx
        mx = 0
        oldest = 0
        for i in xrange(len(eq)):
            if sawHistory[i] > mx:
                mx = sawHistory[i]
                oldest = i

        a = random.choice(eq[oldest])
        if a>0:
            bits[a-1] = 1
        else:
            bits[-a-1] = 0
        return bits





class testFit:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        fit = 0.0
        for var in gene:
            fit-=var*var
            
        return fit


class sphere:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        val = 0.0
        for i in xrange(len(gene)):
            val+=gene[i]**2
        return 1000-math.sqrt(val)

class rosenbrock:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        val = 0.0
        for i in xrange(len(gene)-1):
            val+=(1-gene[i])**2+100*(gene[i+1]-gene[i]**2)**2
        return 1000-val


class kmeansClassify:
    def __init__(self,settings):
        self.settings = settings

        if settings['name'] not in data:
            f = open(settings['name'])
            data[settings['name']] = eval(f.read())
            #print data['temp.txt']['t1'] 
    def evaluate(self,gene):
        objs = {objName:0 for objName in data[self.settings['name']]}
        
        #get Midpoints from data
        midPoints = [copy.deepcopy(data[self.settings['name']][random.choice(data[self.settings['name']].keys())]['data']) for k in xrange(self.settings['k'])]
        #calculate distances
        dist = {objName:[calcDist(data[self.settings['name']][objName]['data'],mid,gene) for mid in midPoints] for objName in objs}

        #assign labels
        for objName in objs:
            objs[objName] = dist[objName].index(min(dist[objName]))
        last = copy.deepcopy(objs)
        conv = False

        while not conv:
            #update midpoints
            midPoints = updateMids(data[self.settings['name']],objs,midPoints)
            #calculate distances
            dist = {objName:[calcDist(data[self.settings['name']][objName]['data'],mid,gene) for mid in midPoints] for objName in objs}
            #reassign labels
            for objName in objs:
                objs[objName] = dist[objName].index(min(dist[objName]))
            #check for changes
            conv = True
            for objName in objs:
                if last[objName]!=objs[objName]:
                    conv = False
                    break
                    
            last = copy.deepcopy(objs)           
        #calculate fitness of final cluster
        pen = 0
        for d in gene:
            if d:
                pen+=1
        

        fit = 0.0
        val = 0
        for i in xrange(len(midPoints)):
            temp = [0 for d in midPoints]
            count =0
            for objName in objs:
                
                if objs[objName]==i:
                    count+=1
                    temp[data[self.settings['name']][objName]['cluster']]+=1 
            if count:
                fit+=(2*max(temp)-sum(temp))#/count
            val+=sum(temp)


        return (fit-pen*.001)#/val

def calcDist(point,mid,gene):
    s = 0.0
    
    for d in xrange(len(gene)):
        if chr(d) in point:
            if chr(d) in mid:
                s+=(point[chr(d)]-mid[chr(d)])**2*gene[d]
            else:
                s+=(point[chr(d)]**2)*gene[d]
        else:
            if chr(d) in mid:
                s+=(mid[chr(d)]**2)*gene[d]
    return math.sqrt(s)


def updateMids(data,objs,mids):
    newMid = [{} for d in mids]



    for i in xrange(len(mids)):
        count = 0
        for objName in objs:
            if objs[objName]==i:
                count+=1
                for j in xrange(256):
                    if chr(j) not in newMid[i]:
                        if chr(j) in data[objName]['data']:
                            newMid[i][chr(j)]=data[objName]['data'][chr(j)]
                        else:
                            newMid[i][chr(j)] = 0.0
                    else:
                        if chr(j) in data[objName]['data']:
                            newMid[i][chr(j)]+=data[objName]['data'][chr(j)]
        if count:
            for j in xrange(256):
                newMid[i][chr(j)]/=count
    #return new mids
    return newMid

