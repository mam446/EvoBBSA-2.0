







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
        self.name = name
        
        self.allMax = None

        self.converge = converge
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
        if gMax:
            self.curRun.append({'evals':state.curEval,'max':gMax.fitness,'ave':ave})
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
                Sum+=r[-1]['max']
                num+=1
        if num==0:
            return False 
        if Sum/num<.1:
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
        num
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['ave']
                num+=1
        return Sum/num
     
    def log(self):
        return

    def plot(self):
        return














