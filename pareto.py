import random


class test:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.distance = None


    def calcDistance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**.5

    def dominate(self,other):
        if self.x>=other.x and self.y>other.y:
            return True
        if self.x>other.x and self.y>=other.y:
            return True
        return False






class pareto:
    def __init__(self,pop):
        
        self.fronts = {}
        self.pop = []    
        i = 0
        while pop:
            pop,self.fronts[i] = self.findTopFront(pop)
            i+=1
        self.fillCrowdingDistance()


    def findTopFront(self,curPop):
        top = []
        for i in xrange(len(curPop)):
            t = True
            for j in xrange(len(curPop)):
                if i==j:
                    continue
                else:
                    if curPop[j].dominate(curPop[i]):
                        t = False
                        break
            if t:
                top.append(curPop[i])
                curPop[i].distance = None
        for ind in top:
            self.pop.append(ind) 
            curPop.remove(ind)
            

        return curPop,top

    def fillCrowdingDistance(self):
        for key in self.fronts.keys():
            for i in xrange(len(self.fronts[key])):
                for j in xrange(i):
                    dis = self.fronts[key][i].calcDistance(self.fronts[key][j])
                    if self.fronts[key][i].distance is None:
                        self.fronts[key][i].distance = dis
                    if self.fronts[key][j].distance is None:
                        self.fronts[key][j].distance = dis
                    if dis< self.fronts[key][i].distance:
                        self.fronts[key][i].distance = dis
                    if dis< self.fronts[key][j].distance:
                        self.fronts[key][j].distance = dis

    def keepMu(self,mu):
        self.pop = []
        cur = 0
        for key in self.fronts.keys():
            if cur <mu: 
                if mu-cur>=len(self.fronts[key]):
                    cur+=len(self.fronts[key])
                else:
                    self.fronts[key].sort(key=lambda x: x.distance,reverse = True)
                    self.fronts[key] = self.fronts[key][:mu-cur]
                    for obj in self.fronts[key]:
                        obj.distance = None
                    cur =mu
            else:
                self.fronts[key] = []
            self.pop.extend(self.fronts[key])
        self.fillCrowdingDistance()

    def getPop(self,mu = None):
        if mu:
            self.keepMu(mu)
        return self.pop

    def tournSelect(self,k):
        cur = None
        s = random.sample(self.pop,k)
        for i in xrange(k):
            if not cur:
                cur = s[i]
            else:
                if s[i].dominate(cur):
                    cur = s[i]
                    continue
                if cur.dominate(s[i]):
                    continue
                if cur.distance<s[i].distance:
                    cur = s[i]
                    continue
                if cur.distance>s[i].distance:
                    continue
                if random.random()>=.5:
                    continue
                cur = s[i]
        return cur











