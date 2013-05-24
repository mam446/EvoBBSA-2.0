import copy
import genNode
import random
import funcs


class kTourn(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['kTourn']) 
        super(kTourn,self).__init__(parent,settings,funcs.kTourn,1,p)


class trunc(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['trunc'])
        super(trunc,self).__init__(parent,settings,funcs.trunc,1,p) 

nodes = [kTourn,trunc]





