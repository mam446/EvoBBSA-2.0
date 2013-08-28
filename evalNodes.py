import funcs
import copy
import genNode

class evaluate(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.solSettings)
        super(evaluate,self).__init__(parent,settings,funcs.evaluate,"Evaluate",1,{})

    def toDict(self):
        return {"Evaluate":[self.down[0].toDict()]}


    def evaluate(self):
        ret =  super(evaluate,self).evaluate()
        self.state.curEval+=len(ret)

        return ret

nodes = [evaluate]
