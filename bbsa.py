import random
import variationNodes
import selectionNodes
import setNodes
import state
import logger

nodes = []

nodes.extend(varationNodes.nodes)
nodes.extend(selectionNodes.nodes)

nodes.extend(setNodes.nodes)




class bbsa:
    def __init__(self,settings):

        self.root = None

        self.depth = 0
        self.size = 0

        self.name = "bbsa"


        self.aveOps = 0.0
        self.aveBest = 0.0
        self.aveEval = 0.0

        self.settings = settings

        self.state = state.state(settings)

        self.initPop = random.randint(1,settings.initPopMax)
        
        self.logger = logger.logger(self.name,settings.bbsaSettings['converge'])

        self.createRandom()



    def createRandom(self,start = None):
        
        size = random.randint(1,2**(self.settings.bbsaSettings['maxDepth']))
        if start ==None:
            start  = self.root
        else:
            size = random.randint(1,self.settings.bbsaSettings['mutateMax'])
        for i in xrange(size):
            node = random.choice(nodes)
            if not start:
                start = node(None,self.settings)
                start.randomize(self.state)
                continue
            last = None
            cur = start
            while cur:
                last = cur
                if not cur.down:
                    break
                cur = random.choice(cur.down)
            if cur==last:
                continue
            cur = last
            n = random.randint(0,len(cur.down)-1)
            cur.down[n] = node(cur,self.settings)
            cur.down[n].randomize(self.state)
        start.fillTerms()
        self.update()
        if self.root == None:
            self.root = start
        self.count()
        return

    def count(self)
        self.size = self.root.count()
        return

    def fillTerms(self):
        self.root.fillTerms(self.state)


    def evaluate(self):
      
        for prob in self.settings.probConf:
            for run in xrange(self.settings.bbsaSettings['runs']):
                self.run()
                self.logger.nextRun()
                self.state.reset()
            self.settings.nextProbConf()
            #self.update()
            self.logger.nextProbConf()
        self.aveBest = self.logger.getAveBest()
        self.aveEvals = self.logger.getAveEvals()
        self.fitness = self.aveBest

    def run(self):
        for it in xrange(self.settings.bbsaSettings['maxIterations']):
            self.root.evaluate()
            logger.nextIter(self.state)
            if state.done():
                break
        logger.nextIter(self.state)


    def update(self):
        self.depth = self.root.update(0,self.state)













