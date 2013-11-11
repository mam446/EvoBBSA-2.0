# cython: profile=True







class logger:
    def __init__(self,name,converge):
        
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.probOps = []
        self.ops = []
        self.name = name
        
        self.converge = converge
        self.allMax = None        
        self.curCon = 0
        self.conVal = 0.0

    def reset(self):
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.probOps = [] 
        self.ops = []
        
        self.allMax = None

        self.curCon = 0
        self.conVal = 0.0
        

    def nextRun(self):
        self.runs.append(self.curRun)
        self.curRun = []
        self.curCon = 0
        self.conVal = 0.0
        self.allMax = None

    def nextProbConf(self):
        self.probConf.append(self.runs)
        self.runs = []
        self.probOps.append(self.ops)
        self.ops = []
        self.curCon = 0
        self.conVal = 0.0
        self.allMax = None

    def nextIter(self,state):
        gMax = None
        Sum = 0.0
        num = 0
        for d in state.pers:
            for ind in state.pers[d]:
                if not gMax or ind.fitness>gMax.fitness:
                    gMax = ind
                Sum+=ind.fitness
                num+=1
        for ind in state.last:
            if not gMax or ind.fitness>gMax.fitness:
                gMax = ind
            Sum+=ind.fitness
            num+=1
        if num:
            ave = Sum/num
        else:
            ave = 0
        if gMax and self.allMax!=None and gMax<=self.allMax:
            self.curCon+=1
        else:
            self.curCon = 0
            if gMax:
                self.allMax = gMax
        if state.bestInd:
            self.curRun.append({'evals':state.curEval,'max':state.bestInd.fitness,'ave':ave})
        else:
            self.curRun.append({'evals':state.curEval,'max':0,'ave':ave})
        self.ops.append(state.curOp)

    def hasConverged(self):
        return self.curCon>=self.converge


    def getAveOps(self):
        Sum = 0.0
        num = 0
        for p in self.probOps:
            for r in p:
                Sum+=r
                num+=1
        return Sum/num


    def valid(self):
        
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                if len(r)-1:
                    Sum+=r[-2]['max']
                num+=1

        if (Sum<.001 and Sum>-.001) or num==0:
            return False 
        return True

    def getAveBest(self):
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['max']
                num+=1
        return Sum/num

    def getAveEvals(self):
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['evals']
                num+=1
        return Sum/num
   
    def getAveAve(self):
        Sum = 0.0
        num = 0.0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['ave']
                num+=1
        return Sum/num
     
    def log(self):
        for i in xrange(len(self.probConf)):
            f = open(self.name+"-"+str(i),'w')
            r = ""
            for x in xrange(len(self.probConf[i])):
                r+=str(x)+"\t"
            w = 'evals\t'+r+"\n"
            
            fm = ""
            fm+=w
            print len(self.probConf[i])
            for j in xrange(len(self.probConf[i][0])):
                line = ""
                for k in xrange(len(self.probConf[i])):
                    if k==0:
                        line+=str(self.probConf[i][k][j]['evals'])+'\t'
                    if i<len(self.probConf[i][k]):
                        line+=str(self.probConf[i][k][j]['max'])+'\t'
                    else:
                        line+='\t'
                line+='\n'
                fm+=line
            f.write(fm)
            f.close()
                        
        return

    def plot(self):
        return














