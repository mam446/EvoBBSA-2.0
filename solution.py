import representations

class solution:

    def __init__(self,solSettings):
        self.settings = solSettings
        
        self.rep = solSettings['repr'] 

        self.gene = representations.reps[self.rep]['gene'](solSettings['settings'])
        self.fitFunc = representations.reps[self.rep][solSettings['prob']]

        self.fitness = 0.0


    def evaluate(self):
        self.fitness = self.fitFunc(self.gene)
        return self.fitness
