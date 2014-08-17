# cython: profile=True
import representations
from copy import deepcopy



class solution:

    def __init__(self,solSettings):
        if isinstance(solSettings,dict):
            self.settings = solSettings
            
            self.rep = solSettings['repr'] 
            self.gene = representations.reps[self.rep]['gene'](solSettings['settings'])
            self.fitFunc = representations.reps[self.rep][solSettings['prob']](solSettings['settings'])

            self.fitness =0.0 

            self.aux = {}
        else:
            self.settings = solSettings.settings
            if isinstance(solSettings.gene,list):
                self.gene = list(solSettings.gene)
            else:
                self.gene = deepcopy(solSettings.gene)
            self.fitFunc = solSettings.fitFunc
            self.fitness = 0.0
            self.aux = dict(solSettings.aux)

    def evaluate(self):
        self.fitness = self.fitFunc.evaluate(self.gene)
        #print self.fitness
        return self.fitness

    def duplicate(self):
        x = solution(self)
        return x

    def __lt__(self,other):
        return self.fitness<other.fitness

    def __gt__(self,other):
        return self.fitness>other.fitness
    
    def __ge__(self,other):
        return self.fitness>=other.fitness
    
    def __le__(self,other):
        return self.fitness<=other.fitness
