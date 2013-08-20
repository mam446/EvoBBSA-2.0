







class logger:
    def __init__(self,name,converge):
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.ops = []
        self.name = name
        
        self.converge = converge
        
        self.curCon = 0
        self.conVal = 0.0

    def reset(self):
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.probOps = [] 
        self.ops = []
        self.name = name
        
        self.converge = converge
        self.curCon = 0
        self.conVal = 0.0
        

    def nextRun(self):
        self.runs.append(self.curRun)
        self.curRun = []
        self.curCon = 0
        self.conVal = 0.0

    def nextProbConf(self):
        self.probConf.append(self.runs)
        self.runs = []
        self.probOps.append(self.ops)
        self.ops = []
        self.curCon = 0
        self.conVal = 0.0

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
        ave = Sum/num
        if gMax.fitness == self.conVal:
            self.curCon+=1 
        self.curRun.append({'evals':state.curEval,'max':gMax.fitness,'ave':ave})
        self.ops.append(state.curOp)

    def hasConverged():
        return self.curCon>=self.converge


    def getAveOps():
        Sum = 0.0
        num = 0
        for p in self.probOps:
            for r in p:
                Sum+=r
                num+=1
        return Sum/num

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














