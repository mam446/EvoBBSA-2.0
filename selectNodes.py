import copy
import genNode
import random
import funcs


class kTourn(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['kTourn']) 
        super(kTourn,self).__init__(parent,settings,funcs.kTourn,"kTourn",1,p)

    def toDict(self):
        return {"kTourn(k="+str(self.params['k']['value'])+",count="+str(self.params['count']['value']):[self.down[0].toDict()]}

class trunc(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['trunc'])
        super(trunc,self).__init__(parent,settings,funcs.trunc,"trunc",1,p) 
    
    def toDict(self):
        return {"trunc(count="+str(self.params['count']['value']):[self.down[0].toDict()]}

nodes = [kTourn,trunc]





