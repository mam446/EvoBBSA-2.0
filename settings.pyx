# cython: profile=True






class runSettings:
    def __init__(self,filename,directory=""):

        self.bbsaSettings = {}

        self.seed = None

        self.nodeSettings = {}
        
        self.solSettings = {}
        
        self.probConf = []

        self.hyperSettings = {}

        self.directory = directory

        """
        #hyper Settings
        self.hyperSettings['mu'] = 100
        self.hyperSettings['lambda'] = 40
        self.hyperSettings['type'] = 'SGA' 
        self.hyperSettings['mpi'] = False
        self.hyperSettings['procs'] = 5
        self.hyperSettings['mateRate'] = .3
        self.hyperSettings['mutateRate'] = .3
        self.hyperSettings['evaluations'] = 5000
        self.hyperSettings['objectives'] = ['evals','fitness','time']
        self.hyperSettings['childK'] = 8
        self.hyperSettings['seed'] = None

        #bbsaSettings
        self.bbsaSettings['time'] = 20
        self.bbsaSettings['maxStartNodes'] = 15            
        self.bbsaSettings['maxEvals'] = 50000
        self.bbsaSettings['maxOps'] = 5000000
        self.bbsaSettings['maxIterations'] = 10000
        self.bbsaSettings['maxDepth'] = 5
        self.bbsaSettings['mutateMax'] = 5
        self.bbsaSettings['runs'] = 5
        self.bbsaSettings['converge'] = 25
        self.bbsaSettings['initPopMax'] = 50
        self.bbsaSettings['representation'] = 'bitString'
        self.bbsaSettings['problem'] = 'dTrap'
        self.bbsaSettings['penalty'] = .001
        #variation node
        self.nodeSettings['mutate'] = {'rate':{'value': 0.0,'range':(0.0,1.0),'type':'float'}}
        self.nodeSettings['mutate']['weight'] = 2
        self.nodeSettings['uniRecomb'] = {'num':{'value': 1,'range':(1,25),'type':'int'}}
        self.nodeSettings['uniRecomb']['weight'] = 2
        self.nodeSettings['diagonal'] = {'n':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['diagonal']['weight'] = 2

        self.nodeSettings['gaussian'] = {'variance':{'value':0.0,'range':(0.0,100),'type':'float'},'rate':{'value':0.0,'range':(0.0,1.0),'type':'float'}}
        self.nodeSettings['gaussian']['weight'] = 2


        
        self.nodeSettings['onePoint'] = {}
        self.nodeSettings['onePoint']['weight'] = 2
    #selection nodes
        self.nodeSettings['kTourn'] = {'count':{'value':1,'range':(1,25),'type':'int'},'k':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['kTourn']['weight'] = 2
        self.nodeSettings['trunc'] = {'count':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['trunc']['weight'] = 2
        
        self.nodeSettings['fitProp'] = {'count':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['fitProp']['weight'] = 2

        self.nodeSettings['randSubset'] = {'count':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['randSubset']['weight'] = 2
        #set Nodes

        self.nodeSettings['makeSet'] = {'name':{'value':"",'type':'str'}}
        self.nodeSettings['makeSet']['weight'] = 2

        #aux Nodes
        self.nodeSettings['forLoop'] = {'count':{'value':1,'range':(1,25),'type':'int'}}
        self.nodeSettings['forLoop']['weight'] = 2
        
        self.nodeSettings['ifConverge'] = {'conv':{'value':5,'range':(5,25),'type':'int'}}
        self.nodeSettings['ifConverge']['weight'] = 2

        #termNodes
        self.nodeSettings['randInd'] = {'count':{'value': 1,'range':(1,25),'type':'int'}}
        self.nodeSettings['randInd']['weight'] = 2
        """
        if filename:
            f = open(filename)
            d = eval(f.read())
            for key in d['nodeSettings']:
                self.nodeSettings[key] = d['nodeSettings'][key]
            for key in d['bbsaSettings']:            
                self.bbsaSettings[key] = d['bbsaSettings'][key]
            for key in d['hyperSettings']:            
                self.hyperSettings[key] = d['hyperSettings'][key]

            self.probConf = d['problems']
        else:

            #self.probConf.append({'weight':1,'repr':'bitString','prob':'allOnes','settings':{'length':210,'name':'apple'}})
            #self.probConf.append({'weight':1,'repr':'bitString','prob':'allOnes','settings':{'length':100,'name':'grape'}})
            self.probConf.append({'weight':1,'repr':'bitString','prob':'dTrap','settings':{'length':100,'k':5}})
            #self.probConf.append({'weight':1,'repr':'bitString','prob':'nk','settings':{'length':100,'dimensions':30,'k':5,'problemSeed':0,'maximumFitness':1.0,'nkProblemFolder':'','run':0}})

        self.solSettings = self.probConf[0]

    def nextProbConf(self):
        x = self.probConf[0]
        self.probConf = self.probConf[1:]
        self.probConf.append(x)
        self.solSettings = self.probConf[0]
        
