# cython: profile=True
import random
import genNode
import copy
import solution

class termNode(genNode.node):
    def __init__(self,parent,settings):
        super(termNode,self).__init__(parent,settings,None,None,0,{})
        self.canTake = [0]
        self.canReturn =[2]

    def evaluate(self):
        if self.name not in self.state.pers:
            self.state.pers[self.name] = []
        return self.state.pers[self.name]

    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        if not self.name:
            self.name = 'A'
        self.state = state
        return self.height

    def makeProg(self,numTab,var):
        tab = "    "
        indent = ""
        for i in xrange(numTab):
            indent+=tab
        prog = "x"+var+"= "+self.name+"\n"+indent
        return prog

    def randomize(self,state):
        if not state.pers.keys():
            state.pers['A'] = []
        opts = state.pers.keys()
        self.name = random.choice(opts)
        self.state = state
        return 


class lastNode(genNode.node):
    def __init__(self,parent,settings):
        super(lastNode,self).__init__(parent,settings,None,None,0,{})
        self.name = 'last'
        self.canTake = [0]
        self.canReturn= [2]


    def evaluate(self):
        return self.state.last

    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height

    def makeProg(self,numTab,var):
        tab = "    "
        indent = ""
        for i in xrange(numTab):
            indent+=tab
        prog = "x"+var+"= "+self.name+"\n"+indent
        return prog

    def randomize(self,state):
        self.state = state
        return


class randomInd(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['randInd'])
        super(randomInd,self).__init__(parent,settings,None,'randInd',0,p)
        self.name = 'randInd'
        self.canTake = [0]
        self.canReturn = [1,2]

    def evaluate(self):
        return [solution.solution(self.settings.solSettings) for i in xrange(self.params['count']['value'])]

    def setTake(self,numerocity):
        super(randomInd,self).setTake(numerocity)
        self.take = [0]
    

    def randomize(self,state):
        super(randomInd,self).randomize(state)
        if self.ret==1:
            self.params['count']['value'] = 1


    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        self.settings = state.settings
        return self.height

single = {'randomInd':randomInd}
multi = {'last':lastNode,'termNode':termNode,'randomInd':randomInd}
