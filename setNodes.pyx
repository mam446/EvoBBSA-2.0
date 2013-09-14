# cython: profile=True
import funcs
import genNode
import copy
import random

class union(genNode.node):
    def __init__(self,parent,settings):
        super(union,self).__init__(parent,settings,funcs.union,"union",2,{})
        self.canTake = [1,2]
        self.canReturn =[2]

    def setTake(self,numerocity):
        super(union,self).setTake(numerocity)
        self.ret = 2
    
    def toDict(self):
        return {"Union":[self.down[0].toDict(),self.down[1].toDict()]}

class makeSet(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['makeSet'])
        super(makeSet,self).__init__(parent,settings,funcs.mutate,"makeSet",1,p)
        self.canTake = [1,2]
        self.canReturn =[1,2]

    def evaluate(self):
        if self.state.curOp>=self.state.maxOp:
            return []
        if self.state.curEval >= self.state.maxEval:
            return []
        
        rDown = self.down[0].evaluate()

        self.state.pers[self.params['name']['value']] = rDown

        self.state.curOp+=len(rDown)*self.opWeight

        return rDown

    def update(self,depth,state):
        d = self.down[0].update(depth+1,state)
        self.depth = depth
        self.height = d+1
        if self.params['name']['value'] not in self.state.pers:
            self.state.pers[self.params['name']['value']] = []
        self.state = state
        return self.height

    def randomize(self,state):
        self.state = state
        opts = self.state.pers.keys()
        if opts and opts[-1]==None:
            opts = opts[:-1]
        if opts:
            opts.append(chr(ord(opts[-1])+1))
        else:
            opts.append('A')
        self.params['name']['value'] = random.choice(opts)
        self.state.pers[self.params['name']['value']] = []
        return

    def toDict(self):
        return {"makeSet {"+self.params['name']['value']+"}":[self.down[0].toDict()]}

    def makeProg(self,numTab,var):
        tab = "    "
        indent = ""
        for i in xrange(numTab):
            indent+=tab
        prog = ""
        prog = self.down[0].makeProg(numTab,var+"0")
        prog+= self.params['name']['value']+" = x"+var+"0\n"+indent
        prog+="x"+var+"=x"+var+"0\n"+indent
        return prog

nodes = [union,makeSet]
single = [makeSet]
multi = [makeSet,union]
