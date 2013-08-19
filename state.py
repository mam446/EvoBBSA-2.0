import termNodes


class state:
    def __init__(self,settings):
        self.pers = {}
        self.curOp = 0
        self.curEval = 0
        self.last = []        
        self.maxOp = settings.bbsaSettings['maxOps']
        self.maxEval = settings.bbsaSettings['maxEvals']

        self.terms = termNodes.nodes

    def reset(self):
        self.curOp = 0
        self.curEval = 0
        for d in self.pers:
            self.pers[d] = []
        self.last = []

    def done(self):
        if self.curOp>=self.maxOp or self.curEval>=self.maxEval:
            return True
        return False


