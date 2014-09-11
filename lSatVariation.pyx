
import random
import genNode
import funcs
import copy



class SAWStats(genNode.node):
    def __init__(self,parent,settings):
        super(SAWStats,self).__init__(parent,settings,funcs.SAWStats,'SAWStats',1,{})
        self.canTake = [1,2]
        self.canReturn = [1,2]

class SAWMutate(genNode.node):
    def __init__(self,parent,settings):
        super(SAWMutate,self).__init__(parent,settings,funcs.SAWMutate,"SAWMutate",1,{})
        self.canTake = [1,2]
        self.canReturn =[1,2]




single = {'SAWStats':SAWStats,'SAWMutate':SAWMutate}        
multi = {'SAWStats':SAWStats,'SAWMutate':SAWMutate}        





