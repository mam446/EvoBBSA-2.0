import random
import genNode
import funcs
import copy

class mutate(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['mutate'])
        super(mutate,self).__init__(parent,settings,funcs.mutate,"mutate",1,p)

    def toDict(self):
        return {"mutate("+str(self.params['rate']['value'])+")":[self.down[0].toDict()]}
         
class uniRecomb(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['uniRecomb'])
        super(uniRecomb,self).__init__(parent,settings,funcs.uniRecomb,"uniRecomb",1,p)

    def toDict(self):
        return {"uniRecomb(count="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}

class diagonal(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['diagonal'])
        super(diagonal,self).__init__(parent,settings,funcs.diagonal,"diagonal",1,p)

    def toDict(self):
        return {"diagonal(n ="+str(self.params['n']['value'])+")":[self.down[0].toDict()]}

nodes = [mutate,uniRecomb,diagonal]

