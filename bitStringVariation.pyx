import random
import genNode
import funcs
import copy


class mutate(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['mutate'])
        super(mutate,self).__init__(parent,settings,funcs.mutate,"mutate",1,p)
        self.canTake = [1,2]
        self.canReturn =[1,2]

    def toDict(self):
        return {"mutate("+str(self.params['rate']['value'])+")":[self.down[0].toDict()]}
         
class uniRecomb(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['uniRecomb'])
        super(uniRecomb,self).__init__(parent,settings,funcs.uniRecomb,"uniRecomb",1,p)
        self.canTake = [2]
        self.canReturn =[2]

    def toDict(self):
        return {"uniRecomb(count="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}


class uniRecomb2(genNode.node):
    def __init__(self,parent,settings):
        super(uniRecomb2,self).__init__(parent,settings,funcs.uniRecomb2,"uniRecomb2",2,{})
        self.canTake = [1]
        self.canReturn =[2]
    
    def setTake(self,numerocity):
        super(uniRecomb2,self).setTake(numerocity)
        self.ret = 2

    def toDict(self):
        return {"uniRecomb2":[self.down[0].toDict(),self.down[1].toDict()]}

class diagonal(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['diagonal'])
        super(diagonal,self).__init__(parent,settings,funcs.diagonal,"diagonal",1,p)
        self.canTake = [2]
        self.canReturn =[2]

    def toDict(self):
        return {"diagonal(n ="+str(self.params['n']['value'])+")":[self.down[0].toDict()]}

class onePoint(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['onePoint'])
        super(onePoint,self).__init__(parent,settings,funcs.onePoint,"onePoint",2,p)
        self.canTake = [1]
        self.canReturn = [2]

    def setTake(self,numerocity):
        super(onePoint,self).setTake(numerocity)
        self.ret = 2

    def toDict(self):
        return {"onePoint":[self.down[0].toDict(),self.down[1].toDict()]}




nodes = [mutate,uniRecomb,diagonal,onePoint,uniRecomb2]
single = [mutate]        
multi = [mutate,uniRecomb,diagonal,onePoint,uniRecomb2]


