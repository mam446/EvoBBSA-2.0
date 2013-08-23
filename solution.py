import representations
import copy



class solution:

    def __init__(self,solSettings):
        self.settings = solSettings
        
        self.rep = solSettings['repr'] 

        self.gene = representations.reps[self.rep]['gene'](solSettings['settings'])
        self.fitFunc = representations.reps[self.rep][solSettings['prob']](solSettings['settings'])

        self.fitness = 0.0


    def evaluate(self):
        self.fitness = self.fitFunc.evaluate(self.gene)
        return self.fitness

    def duplicate(self):
        return copy.deepcopy(self)

    def __lt__(self,other):
        return self.fitness<other.fitness

    def __gt__(self,other):
        return self.fitness>other.fitness
    
    def __ge__(self,other):
        return self.fitness>=other.fitness
    
    def __le__(self,other):
        return self.fitness<=other.fitness
