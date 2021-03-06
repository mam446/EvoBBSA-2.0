# cython: profile=True
import funcs
import copy
import genNode

class evaluate(genNode.node):
    def __init__(self,parent,settings):
        super(evaluate,self).__init__(parent,settings,funcs.evaluate,"evaluate",1,{})
        self.params.update({'state':self.state})
        self.canTake = [1,2]
        self.canReturn =[1,2]



    def makeProg(self,numTab,var):
        #prog = super(evaluate,self).makeProg(numTab,var)
        tab = "    "
        indent = numTab*tab
        prog = ""
        prog+= self.down[0].makeProg(numTab,var+'0')
        prog += 'x'+var+" = evaluate([x"+var+"0],{\'state\':bestLog})\n"+indent
        prog+= "evals+=len(x"+var+")"+'\n'+indent
        return prog


    def evaluate(self):
        #self.params['state'] = self.state
        ret =  super(evaluate,self).evaluate()
        self.state.curEval+=len(ret)
        return ret

nodes = [evaluate]

single = {'bitString':{'evaluate':evaluate},'realValued':{'evaluate':evaluate}}
multi = {'bitString':{'evaluate':evaluate},'realValued':{'evaluate':evaluate}}


