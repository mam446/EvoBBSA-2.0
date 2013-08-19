import random


class node(object):

    def __init__(self,parent,settings,func,name,children=1,params= {}):
        self.depth = 0
        self.height = 0

        self.settings = settings
    
        self.function = func
        self.name = name
    
        self.params = params
        if 'weight' in params: 
            self.opWeight = params['weight']
        else:
            self.opWeight = 1

        self.parent = parent
        if parent:
            self.depth = self.parent.depth+1
        self.down = [None for i in xrange(children)]
    
        self.state = None
        if parent:
            self.state = self.parent.state



    def evaluate(self):
        if self.state.curOp>=self.state.maxOp:
            return []
        if self.state.curEval>=self.state.maxEval:
            return []
        rDown = []
    
        for d in self.down:
            rDown.append(d.evaluate())
            self.state.curOp+=len(rDown[-1])*self.opWeight
        return self.func(rDown,self.param,settings.solSettings)
    
    def update(self,depth,state):
        d = [i.update(depth+1,state) for i in self.down]
        d.append(-1)
        self.depth = depth
        self.height = max(d)+1
        self.state = state
        return self.height

    def randomize(self,state):
        for p in self.params:
            if p == 'weight':
                continue
            if self.params[p]['type'] == 'int':
                self.params[p]['value'] =  random.randint(self.params[p]['range'][0],self.params[p]['range'][1])
            elif self.params[p]['type'] == 'float':
                self.params[p]['value'] = random.random()*(self.params[p]['range'][1]-self.params[p]['range'][0])+self.params[p]['range'][0]
            else:
                raise "Error: No type"


    def makeProg(self,numTab,var):
        tab = "    "
        indent = ""
        for i in xrange(numTab):
            indent+=tab
        prog = ""
        dList = "["
        for d in xrange(len(self.down)):
            prog+=self.down[d].makeProg(numTab,var+str(d))
            dlist+=var+str(d)+","
        dList[-1] = "]"

        pList = "{"
        for p in self.params:
            pList+="\'"+p+"\':"+str(self.params[p]['value'])+","
        pList[-1] = "}"

        prog+="x"+var+" = "+self.name+"("+dList+","+pList+")\n"+indent



    def fillTerms(self,state):
        for i in xrange(len(self.down)):
            if self.down[i]:
                self.down[i].fillTerms(state)
            else:
                self.down[i] = random.choice(state.terms)(self,self.settings)
                self.down[i].randomize(state)

    def count(self):
        t = 1 
        for d in self.down:
            t+=d.count()
        return t
