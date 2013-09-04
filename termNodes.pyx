# cython: profile=True
import random
import genNode


class termNode(genNode.node):
    def __init__(self,parent,settings):
        super(termNode,self).__init__(parent,settings,None,None,0,{})
      

    def evaluate(self):
        if self.name not in self.state.pers:
            self.state.pers[self.name] = []
        return self.state.pers[self.name]

    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        if state.pers.keys():
            state.pers['A'] = []
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

    def toDict(self):
        return self.name

class lastNode(termNode):
    def __init__(self,parent,settings):
        super(lastNode,self).__init__(parent,settings)
        self.name = 'last'


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

    def toDict(self):
        return 'last'

nodes =[lastNode,termNode]
