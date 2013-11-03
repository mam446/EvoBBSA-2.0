import math

#cython: profile=True
data = {}

class allOnes:
    def __init__(self,settings):
        self.settings = settings
        #this is how you store auxiliarly data that everyone can use 
        if settings['name'] not in data:
            data[settings['name']] = [1,2,3,4,5]
    def evaluate(self,gene):
        fit = 0.0
        for bit in gene:
            if bit==1:
                fit+=1.0
        return fit/len(gene)

class testFit:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        fit = 0.0
        for var in gene:
            fit-=var*var
            
        return fit


class sphere:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        val = 0.0
        for i in xrange(len(gene)):
            val+=gene[i]**2
        return 1000-math.sqrt(val)

class rosenbrock:
    def __init__(self,settings):
        self.settings = settings

    def evaluate(self,gene):
        val = 0.0
        for i in xrange(len(gene)-1):
            val+=(1-gene[i])**2+100*(gene[i+1]-gene[i]**2)**2
        return 1000-val


class kmeansClassify:
    def __init__(self,settings):
        self.settings = settings

        if settings['name'] not in data:
            f = open(settings['name'])
            data[settings['name']] = eval(f.read())
    
    def evaluate(self,gene):

        return 0.0








