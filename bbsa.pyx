# cython: profile=True
import copy
import random
import evalNodes
import variationNodes
import selectNodes
import setNodes
import state
import logger
import solution

nodes = []
single = []
multi = []

nodes.extend(variationNodes.nodes)
nodes.extend(selectNodes.nodes)
nodes.extend(evalNodes.nodes)
nodes.extend(setNodes.nodes)

single.extend(variationNodes.single)
single.extend(selectNodes.single)
single.extend(evalNodes.single)
single.extend(setNodes.single)

multi.extend(variationNodes.multi)
multi.extend(selectNodes.multi)
multi.extend(evalNodes.multi)
multi.extend(setNodes.multi)


def popNodes(node,a):
    a.append(node)
    for x in node.down:
        popNodes(x,a)


class bbsa:
    def __init__(self,settings):

        self.root = None

        self.depth = 0
        self.size = 0

        self.name = "Default"


        self.aveOps = 0.0
        self.aveBest = 0.0
        self.aveEval = 0.0

        self.fitness = 0.0

        self.settings = settings

        self.state = state.state(settings)

        self.initPop = random.randint(1,settings.bbsaSettings['initPopMax'])
        
        self.logger = logger.logger(self.name,settings.bbsaSettings['converge'])

        self.createRandom()



    def createRandom(self,start = None):
        
        size = random.randint(1,(self.settings.bbsaSettings['maxStartNodes']))
        if start ==None:
            start  = self.root
        else:
            size = random.randint(1,self.settings.bbsaSettings['mutateMax'])
            for s in xrange(len(start.down)):
                start.down[s] = None
        for i in xrange(size):
            node = random.choice(nodes)
            if not start:
                node = random.choice(nodes)
                start = node(None,self.settings)
                start.setTake(max(start.canTake))
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
            if cur.take[n]==2:
                node = random.choice(multi)
                cur.down[n] = node(cur,self.settings)
                
                cur.down[n].setTake(max(cur.down[n].canTake))
                cur.down[n].randomize(self.state)
            else:
                node = random.choice(single)
                cur.down[n] = node(cur,self.settings)
                cur.down[n].setTake(1)
                cur.down[n].randomize(self.state)
        start.fillTerms(self.state)
        if self.root == None:
            self.root = start
        self.update()
        self.count()
        return

    def count(self):
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
        self.aveEval = self.logger.getAveEvals()
        self.aveOps = self.logger.getAveOps()
        self.fitness = self.aveBest

    def run(self):
        self.state.last = [solution.solution(self.settings.solSettings) for i in xrange(self.initPop)]

        for it in xrange(self.settings.bbsaSettings['maxIterations']):
            self.state.last = self.root.evaluate()
            self.logger.nextIter(self.state)
            if self.state.done() or self.logger.hasConverged():
                break
        self.state.lastEval()
        self.logger.nextIter(self.state)
    
    def randomNode(self):
        z = []
        popNodes(self.root,z)
        n = random.choice(z)
        return n

    def count(self):
        self.size = self.root.count()

    def update(self):
        self.depth = self.root.update(0,self.state)


    def toDict(self):
        return self.root.toDict()

    def makeProg(self):
        prog = "import random\nfrom funcs import *\n"

        prog+="\n\n"+str(self.toDict())+"\n"
        prog += "\n\nevals = "+str(self.aveEval)
        prog += "\n\nops = "+str(self.aveOps)
        prog += "\n\nfit = "+str(self.fitness)
        prog += "\n\nseed = "+str(self.settings.seed)
        prog += "\n\nbbsaSettings = "+str(self.settings.bbsaSettings)
        prog += "\n\nnodeSettings = "+str(self.settings.nodeSettings)
        prog += "\n\nsolSettings = "+str(self.settings.solSettings)
        prog += "\n\ndef run():\n\t"
       
        for s in self.state.pers:
            prog+=s+" = []\n\t"

        prog += "\n\n\tlast = [solution.solution(solSettings) for i in xrange("+str(self.initPop)+")]\n"


        prog+="\n\tfor i in xrange(bbsaSettings[\'maxEvals\']:\n\t\t" 
        prog+=self.root.makeProg(2,"0")
        prog+="last = x0\n\n\t"
        for s in self.state.pers:
            prog+="last.extend("+s+")\n\t"
        prog+="for ind in last:\n\t\t"
        prog+="ind.evaluate()\n\t"
        prog+="return last\n\n"
        
        return prog

    def valid(self):
        return self.logger.valid() and self.evalExist()

    def altMutate(self):
        x = self.duplicate()
        n =x.randomNode()
        n.randomize(x.state)
        return x

    def evalExist(self):
        ns =[]
        popNodes(self.root,ns)
        found = False

        for n in ns:
            if n.name =="Evaluate":
                found = True
                break
        return found


    def duplicate(self):
        x = copy.deepcopy(self)
        
        x.aveOps = 0.0
        x.aveBest = 0.0
        x.aveEval = 0.0

        
        x.logger = logger.logger(self.name,self.settings.bbsaSettings['converge'])

        x.state.reset()
        x.state.settings = x.settings
        x.fitness = 0
        x.update()
        return x

    def mutate(self):
        x = self.duplicate()
        n = x.randomNode()
        self.createRandom(n)
        x.update()
        x.count()
        return x

    def mate(self, other):
        x = self.duplicate()
        y = other.duplicate()
      
        xn = x.randomNode()
        yn = y.randomNode()
        while xn.ret!=yn.ret:

            xn = x.randomNode()
            yn = y.randomNode()

        xp = xn.parent
        yp = yn.parent
        if yp is not None:
            if yn==yp.down[0]:
                yp.down[0] = xn
            else:
                
                try:
                    yp.down[1] = xn
                except IndexError:
                    print yp.down
        else:
            y.root = xn

        if xp is not None:
            if xn==xp.down[0]:
                xp.down[0] = yn
            else:
                xp.down[1] = yn
        else:
            x.root = yn

        xn.parent = yp
        yn.parent = xp
        x.update()
        y.update()
        x.count()
        y.count()
        
        return x,y        

    def __gt__(self,other):
        s = self.fitness - .001*self.size
        o = other.fitness - .001*other.size

        return s>o



