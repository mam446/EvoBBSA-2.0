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

    def toDict(self):
        return {"kTourn(k="+str(self.params['k']['value'])+",count="+str(self.params['count']['value']):[self.down[0].toDict()]}

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

    def toDict(self):
        return {"trunc(count="+str(self.params['count']['value']):[self.down[0].toDict()]}

nodes = [kTourn,trunc]

single = [kTourn,trunc]
multi = [kTourn,trunc]



