# cython: profile=True
import copy
import genNode
import random
import funcs


class kTourn(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['kTourn'])
        super(kTourn,self).__init__(parent,settings,funcs.kTourn,"kTourn",1,p)
        self.canTake = [1,2]
        self.canReturn =[1,2]

    def setTake(self,numerocity):
        super(kTourn,self).setTake(numerocity)
        self.take = [2]

    def randomize(self,state):
        super(kTourn,self).randomize(state)
        if self.ret==1:
            self.params['count']['value'] = 1


class trunc(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['trunc'])
        super(trunc,self).__init__(parent,settings,funcs.trunc,"trunc",1,p) 
        self.canTake = [1,2]
        self.canReturn =[1,2]
   
    def setTake(self,numerocity):
        super(trunc,self).setTake(numerocity)
        self.take = [2]
    
    def randomize(self,state):
        super(trunc,self).randomize(state)
        if self.ret==1:
            self.params['count']['value'] = 1



class randSubset(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['randSubset'])
        super(randSubset,self).__init__(parent,settings,funcs.randSubset,"randSubset",1,p) 
        self.canTake = [1,2]
        self.canReturn =[1,2]
   
    def setTake(self,numerocity):
        super(randSubset,self).setTake(numerocity)
        self.take = [2]
    
    def randomize(self,state):
        super(randSubset,self).randomize(state)
        if self.ret==1:
            self.params['count']['value'] = 1




class fitProp(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['fitProp'])
        super(fitProp,self).__init__(parent,settings,funcs.fitProp,"fitProp",1,p) 
        self.canTake = [1,2]
        self.canReturn =[1,2]
   
    def setTake(self,numerocity):
        super(fitProp,self).setTake(numerocity)
        self.take = [2]
    
    def randomize(self,state):
        super(fitProp,self).randomize(state)
        if self.ret==1:
            self.params['count']['value'] = 1











single = {'bitString':{'kTourn':kTourn,'trunc':trunc,'randSubset':randSubset},'realValued':{'kTourn':kTourn,'trunc':trunc,'randSubset':randSubset}}
multi = {'bitString':{'kTourn':kTourn,'trunc':trunc,'randSubset':randSubset},'realValued':{'kTourn':kTourn,'trunc':trunc,'randSubset':randSubset}}



