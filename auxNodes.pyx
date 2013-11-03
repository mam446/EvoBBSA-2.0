#cython: profile=True

import genNode
import random
import copy



class forLoop(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['forLoop'])
        super(forLoop,self).__init__(parent,settings,None,'for',1,p)
        self.canTake = [1]
        self.canReturn = [2]
        self.take = [1]
        self.ret = 2


    def toDict(self):
        return {"For:"+str(self.params['count']['value']):[self.down[0].toDict()]}


    def setTake(self,numerocity):
        self.take = [1]


    def evaluate(self):
        cdef int i
        if self.state.curOp>=self.state.maxOp:
            return []
        if self.state.curEval>=self.state.maxEval:
            return []
             
        ret = []
        f = ret.extend
        d = self.down[0]
        for i in xrange(self.params['count']['value']):
            f(d.evaluate())
        return ret

    def makeProg(self,numTab,var):
        tab = "    "
        indent = tab*numTab
        prog = 'x'+var+" = []\n"+indent
        prog += "for i"+var[1:]+" in xrange("+str(self.params['count']['value'])+"):\n"+indent+tab
        prog+=self.down[0].makeProg(numTab+1,var+str(0))
        prog+="if x"+var+'0:\n'+indent+tab*2
        prog+='x'+var+".append(x"+var+'0[0])\n'+indent
        return prog

single = {'bitString':[],'realValued':[]}
multi = {'bitString':[forLoop],'realValued':[forLoop]}




















