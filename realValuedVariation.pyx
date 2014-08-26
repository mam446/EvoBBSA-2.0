import random
import genNode
import copy
import funcs



class gaussian(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['gaussian'])
        super(gaussian,self).__init__(parent,settings,funcs.gaussian,"gaussian",1,p)
        self.canTake = [1,2]
        self.canReturn = [1,2]


class uniRecomb(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['uniRecomb'])
        super(uniRecomb,self).__init__(parent,settings,funcs.uniRecomb,"uniRecomb",1,p)
        self.canTake = [2]
        self.canReturn =[2]


class diagonal(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['diagonal'])
        super(diagonal,self).__init__(parent,settings,funcs.diagonal,"diagonal",1,p)
        self.canTake = [2]
        self.canReturn =[2]


class onePoint(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['onePoint'])
        super(onePoint,self).__init__(parent,settings,funcs.onePoint,"onePoint",2,p)
        self.canTake = [1]
        self.canReturn = [2]

    def setTake(self,numerocity):
        super(onePoint,self).setTake(numerocity)
        self.ret = 2


single = {'gaussian':gaussian}
multi = {'gaussian':gaussian,'uniRecomb':uniRecomb}


