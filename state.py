import termNodes
import selectNodes

class state:
    def __init__(self,settings=None):
        self.pers = {}
        self.curOp = 0
        self.curEval = 0
        self.last = []        
        if settings:
            self.maxOp = settings.bbsaSettings['maxOps']
            self.maxEval = settings.bbsaSettings['maxEvals']
        self.run = 0
        self.terms = termNodes.multi
        self.sTerms = termNodes.single
        self.settings = settings
        self.reducers = selectNodes.multi[self.settings.bbsaSettings['representation']]
        self.bestInd = None
        self.log = {}
        self.logger = None

    def reset(self):
        self.curOp = 0
        self.curEval = 0
        for d in self.pers:
            self.pers[d] = []
        self.last = []
        self.run = 0
        self.besetInd = None
        self.log = {}

    def done(self):
        if  self.curEval>=self.maxEval:
            return True
        return False

    def lastEval(self):
        for d in self.pers:
            for ind in self.pers[d]:
                ind.evaluate()
        for q in self.last:
            q.evaluate()
        self.run+=1

    def bestSoFar(self,ind):
        if not self.bestInd or self.bestInd.fitness<ind.fitness:
            self.bestInd = ind
            self.log[self.curEval] = ind.fitness

    def logBestSoFar(self,i=0,name='',j = 0):
        f = open("bsf-"+name+'-'+str(j)+"-"+str(i)+".txt",'w')
        k = self.log.keys()
        k.sort() 
        for d in k:
            f.write(str(d)+"\t"+str(self.log[d])+"\n")


        f.close()
