



class allOnes:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        fit = 0.0
        for bit in gene:
            if bit==1:
                fit+=1.0
        return fit/len(gene)




