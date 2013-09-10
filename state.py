import termNodes


class state:
    def __init__(self,settings):
        self.pers = {}
        self.curOp = 0
        self.curEval = 0
        self.last = []        
        self.maxOp = settings.bbsaSettings['maxOps']
        self.maxEval = settings.bbsaSettings['maxEvals']
        self.run = 0
        self.terms = termNodes.nodes
        self.settings = settings
    
    def reset(self):
        self.curOp = 0
        self.curEval = 0
        for d in self.pers:
            self.pers[d] = []
        self.last = []
        self.run = 0
    
    def done(self):
        if self.curOp>=self.maxOp or self.curEval>=self.maxEval:
            return True
        return False

    def lastEval(self):
        for d in self.pers:
            for ind in self.pers[d]:
                ind.evaluate()
        for ind in self.last:
            ind.evaluate()
        self.run+=1

