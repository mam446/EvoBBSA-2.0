import termNodes


class state:
    def __init__(self,settings):
        self.pers = {}
        self.curOp = 0
        self.curEval = 0
        self.last = []        
        self.maxOp = settings.bbsaSettings['maxOps']
        self.maxEval = settings.bbsaSettings['maxEvals']
        run = 0
        self.terms = termNodes.nodes

    def reset(self):
        self.curOp = 0
        self.curEval = 0
        for d in self.pers:
            self.pers[d] = []
        self.last = []
        run = 0

    def done(self):
        if self.curOp>=self.maxOp or self.curEval>=self.maxEval:
            return True
        return False

    def lastEval(self):
        for d in self.pers:
            for ind in self.pers[d]:
                ind.evaluate(False)
        for ind in self.last:
            ind.evaluate(False)
        run+=1


