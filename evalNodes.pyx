# cython: profile=True
import funcs
import copy
import genNode

class evaluate(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.solSettings)
        super(evaluate,self).__init__(parent,settings,funcs.evaluate,"evaluate",1,{})
        self.canTake = [1,2]
        self.canReturn =[1,2]


    def toDict(self):
        return {"Evaluate":[self.down[0].toDict()]}

    def makeProg(self,numTab,var):
        prog = super(evaluate,self).makeProg(numTab,var)
        tab = "    "
        indent = numTab*tab
        prog+= "evals+=len(x"+var+")"+'\n'+indent
        return prog
    def evaluate(self):
        ret =  super(evaluate,self).evaluate()
        self.state.curEval+=len(ret)

        return ret

nodes = [evaluate]

single = [evaluate]
multi = [evaluate]


