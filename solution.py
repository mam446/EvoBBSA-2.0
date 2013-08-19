
import probSols

class solution:

    def __init__(self,solSettings):
        self.settings = solSettings
        self.bits = [random.choice([True,False])for x in xrange(self.settings['length'])]
        


