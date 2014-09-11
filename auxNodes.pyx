#cython: profile=True

import genNode
import random
import copy
import funcs


class ifConverge(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['ifConverge'])
        super(ifConverge,self).__init__(parent,settings,None,'ifConverge',2,p)
        self.canTake = [1,2]
        self.canReturn = [2]

    def evaluate(self):
        if self.state.logger.countConverged()>=self.params['conv']['value']:
            if self.params['reset']['value']:
                self.state.logger.curCon = 0
            return self.down[1].evaluate()
        else:
            return self.down[0].evaluate()
   
   
    def makeProg(self,numTab,var):  
        tab = "    "
        indent = tab*numTab
        prog= 'x'+var+" =  []\n"+indent
        prog+="if log.countConverged() >= "+str(self.params['conv']['value'])+":\n"+indent+tab
        prog+=self.down[1].makeProg(numTab+1,var+str(1))
        prog+='x'+var +" = x"+var+"1\n"+indent
        #remove extra indent
        prog+="else:\n"+indent+tab
        prog+=self.down[0].makeProg(numTab+1,var+str(1))
        prog+='x'+var +" = x"+var+"0\n"+indent

        return prog





class forLoop(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['forLoop'])
        super(forLoop,self).__init__(parent,settings,None,'forLoop',1,p)
        self.canTake = [1]
        self.canReturn = [2]
        self.take = [1]
        self.ret = 2


    def setTake(self,numerocity):
        self.take = [1]


    def evaluate(self):
        cdef int i
             
        ret = []
        f = ret.extend
        d = self.down[0]
        for i in xrange(self.params['count']['value']):
            if self.state.curOp>=self.state.maxOp:
                return []
            if self.state.curEval>=self.state.maxEval:
                return []
            f(d.evaluate())
        return ret

    def makeProg(self,numTab,var):
        tab = "    "
        indent = tab*numTab
        prog = 'x'+var+" = []\n"+indent
        prog += "for d0"+var[1:]+" in xrange("+str(self.params['count']['value'])+"):\n"+indent+tab
        prog+=self.down[0].makeProg(numTab+1,var+str(0))
        prog+="if x"+var+'0:\n'+indent+tab*2
        prog+='x'+var+".append(x"+var+'0[0])\n'+indent
        return prog


class clearAux(genNode.node):
    def __init__(self,parent,settings):
        super(clearAux,self).__init__(parent,settings,funcs.clearAux,'clearAux',1,{})
        self.canTake = [1,2]
        self.canReturn = [1,2]



class normFitness(genNode.node):
    def __init__(self,parent,settings):
        super(normFitness,self).__init__(parent,settings,funcs.normFitness,'normFitness',1,{})
        self.canTake = [1,2]
        self.canReturn = [1,2]










single = {'bitString':{},'realValued':{'clearAux':clearAux,'normFitness':normFitness}}
multi = {'bitString':{'forLoop':forLoop,'ifConverge':ifConverge},'realValued':{'forLoop':forLoop,'clearAux':clearAux,'normFitness':normFitness,'ifConverge':ifConverge}}




















