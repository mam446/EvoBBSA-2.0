






class runSettings:
    def __init__(self,filename = None):

        self.bbsaSettings = {}


        self.nodeSettings = {}
        
        self.solSettings = {}
        
        self.probConf = []


        if not filename:
            
            self.bbsaSettings['maxEvals'] = 50000
            self.bbsaSettings['maxOps'] = 5000000
            self.bbsaSettings['maxIterations'] = 10000
            self.bbsaSettings['maxDepth'] = 5
            self.bbsaSettings['mutateMax'] = 5
            self.bbsaSettings['runs'] = 5
            self.bbsaSettings['converge'] = 25
            self.bbsaSettings['initPopMax'] = 50

            #variation node
            self.nodeSettings['mutate'] = {'rate':{'value': 0.0,'range':(0.0,1.0),'type':'float'}}
            self.nodeSettings['mutate']['weight'] = 2
            self.nodeSettings['uniRecomb'] = {'num':{'value': 1,'range':(1,25),'type':'int'}}
            self.nodeSettings['uniRecomb']['weight'] = 2
            self.nodeSettings['diagonal'] = {'n':{'value':1,'range':(1,25),'type':'int'}}
            self.nodeSettings['diagonal']['weight'] = 2

        #selection nodes
            self.nodeSettings['kTourn'] = {'count':{'value':1,'range':(1,25),'type':'int'},'k':{'value':1,'range':(1,25),'type':'int'}}
            self.nodeSettings['kTourn']['weight'] = 2
            self.nodeSettings['trunc'] = {'count':{'value':1,'range':(1,25),'type':'int'}}
            self.nodeSettings['trunc']['weight'] = 2

            self.nodeSettings['makeSet'] = {'name':{'value':"",'type':'str'}}


            self.probConf.append({'weight':None,'repr':'bitstring','prob':'dTrap','length':100,'trapSize':5})
            self.probConf.append({'weight':None,'repr':'bitstring','prob':'allOnes','length':210})
        
        self.solSettings = self.probConf[0]

    def nextProbConf(self):
        x = self.probConf[0]
        self.probConf = self.probConf[1:]
        self.probConf.append(x)
        
