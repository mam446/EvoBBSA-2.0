# cython: profile=True
import time
import copy
import random
import evalNodes
import variationNodes
import selectNodes
import setNodes
import auxNodes
import termNodes
import state
import logger
import solution
import pygraphviz as pg
import subprocess
import numpy as np
import matplotlib.pyplot as plt

nodes = {'bitString':[],'realValued':[]}
single = {'bitString':[],'realValued':[]}
multi = {'bitString':[],'realValued':[]}
global id
id = 0

#nodes.extend(variationNodes.nodes)
#nodes.extend(selectNodes.nodes)
#nodes.extend(evalNodes.nodes)
#nodes.extend(setNodes.nodes)

single['bitString'].extend(variationNodes.single['bitString'])
single['bitString'].extend(selectNodes.single['bitString'])
single['bitString'].extend(evalNodes.single['bitString'])
single['bitString'].extend(setNodes.single['bitString'])
single['bitString'].extend(auxNodes.single['bitString'])

single['realValued'].extend(variationNodes.single['realValued'])
single['realValued'].extend(selectNodes.single['realValued'])
single['realValued'].extend(evalNodes.single['realValued'])
single['realValued'].extend(setNodes.single['realValued'])
single['realValued'].extend(auxNodes.single['realValued'])

multi['bitString'].extend(variationNodes.multi['bitString'])
multi['bitString'].extend(selectNodes.multi['bitString'])
multi['bitString'].extend(evalNodes.multi['bitString'])
multi['bitString'].extend(setNodes.multi['bitString'])
multi['bitString'].extend(auxNodes.multi['bitString'])

multi['realValued'].extend(variationNodes.multi['realValued'])
multi['realValued'].extend(selectNodes.multi['realValued'])
multi['realValued'].extend(evalNodes.multi['realValued'])
multi['realValued'].extend(setNodes.multi['realValued'])
multi['realValued'].extend(auxNodes.multi['realValued'])

def popNodes(node,a):
    a.append(node)
    for x in node.down:
        popNodes(x,a)


class bbsa:
    def vectorize(self):
        d = {}
        v = []
        for node in multi[self.settings.bbsaSettings['probType']]:
            name = node(None,self.settings).name
            d[name] = 0
        for key in single[self.settings.bbsaSettings['probType']]:
            name = node(None,self.settings).name
            d[name] = 0

        for node in termNodes.multi:
            name = node(None,self.settings).name
            d[name] = 0
        for key in termNodes.single:
            name = node(None,self.settings).name
            d[name] = 0
        a = []
        popNodes(self.root,a)
        for node in a:
            if node.name in d:
                d[node.name]+=1
            
        keys = d.keys()
        keys.sort()
        for k in keys:
            v.append(d[k]) 

        return v


    def check(self):
        A = []
        popNodes(self.root,A)

        for parent in A:
            if not parent.down:
                continue
            for child in parent.down:
                if child.parent != parent:
                    print self.toDict()
                    print parent
                    print child
                    raw_input("this is where I broke")
                    return False
        return True
    
    def __init__(self,settings):

        self.root = None

        self.depth = 0
        self.size = 0

        global id
        self.name="bbsa-"+str(id)
        id+=1


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
            if not start:
                node = random.choice(multi[self.settings.bbsaSettings['probType']])
                start = node(None,self.settings)
                start.setTake(max(start.canTake))
                start.randomize(self.state)
                continue
            nex = None
            cur = start
            while cur:
                nex = random.choice(cur.down)
                if not nex:
                    break
                cur = nex
            
            n = random.randrange(0,len(cur.down))
            while cur.down[n]!=nex:
                n = random.randrange(0,len(cur.down))
            if n <0 or n>1:
                raw_input("fail")
            if cur.take[n]==2:
                node = random.choice(multi[self.settings.bbsaSettings['probType']])
                cur.down[n] = node(cur,self.settings)
                
                cur.down[n].setTake(max(cur.down[n].canTake))
                cur.down[n].randomize(self.state)
            else:
                node = random.choice(single[self.settings.bbsaSettings['probType']])
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
        start = time.time() 
        s = 0
        for prob in self.settings.probConf:
            for run in xrange(self.settings.bbsaSettings['runs']):
                self.run()
                self.logger.nextRun()
                s = len(self.state.last)
                for d in self.state.pers:
                    s+=len(self.state.pers[d])
                self.state.reset()
            self.settings.nextProbConf()
            #self.update()
            self.logger.nextProbConf()
        self.aveBest = self.logger.getAveBest()
        self.aveEval = self.logger.getAveEvals()
        self.aveOps = self.logger.getAveOps()
        self.fitness = self.aveBest
        end = time.time()
        st = ""
        self.time = end-start
        v = self.vectorize()
        for item in v:
            st+=str(item)+", "
        
        """print str(end-start)+", "+str(s)+", "+st         
        if end-start>30:
            self.name +="-long"+str(int(end-start))
            self.makeGraph()"""


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
        tab = "    "
        prog = "import random\nfrom funcs import *\nimport state\n"

        prog+="\n\n"+str(self.toDict())+"\n"
        prog+="\n\ntime = "+str(self.time)
        prog += "\n\nevals = "+str(self.aveEval)
        prog += "\n\nops = "+str(self.aveOps)
        prog += "\n\nfit = "+str(self.fitness)
        prog += "\n\nseed = "+str(self.settings.seed)
        prog += "\n\nbbsaSettings = "+str(self.settings.bbsaSettings)
        prog += "\n\nnodeSettings = "+str(self.settings.nodeSettings)
        prog += "\n\nsolSettings = "+str(self.settings.solSettings)
        prog += "\n\ndef run(numRuns,log,sol=solSettings,name='',progConf=None):\n"+tab
        prog += "for i in xrange(numRuns):\n"+tab*2
        for s in self.state.pers:
            prog+=str(s)+" = []\n"+tab*2
        prog += "evals = 0\n"+tab*2
        prog += "last = [solution.solution(sol) for j in xrange("+str(self.initPop)+")]\n"+tab*2

        prog += "bestLog = state.state()\n"+tab*2
        prog+="while evals< bbsaSettings[\'maxEvals\']:\n"+tab*3 
        prog+=self.root.makeProg(3,"0")
        prog+="last = x0\n\n"+tab*3
        prog+="st = state.state()\n"+tab*3
        prog+="st.last = last\n"+tab*3
        for s in self.state.pers:
            prog+="st.pers[\'"+s+"\'] = "+s+"\n"+tab*3
        prog+="st.curEval = evals\n"+tab*3
        prog+="log.nextIter(st)\n"+tab*2
        for s in self.state.pers:
            prog+="last.extend("+s+")\n"+tab*2
        prog+="for ind in last:\n"+tab*3
        prog+="ind.evaluate()\n"+tab*2
        prog+="st = state.state()\n"+tab*2
        prog+="st.last = last\n"+tab*2
        for s in self.state.pers:
            prog+="st.pers[\'"+s+"\'] = "+s+"\n"+tab*2
        prog+="st.curEval = evals\n"+tab*2
        prog+="log.nextIter(st)\n"+tab*2
        prog+="print i\n"+tab*2
        prog+="log.nextRun()\n"+tab*2
        prog+="bestLog.logBestSoFar(i,name,progConf)\n"+tab*2
        prog+="bestLog.reset()\n"+tab
        prog+="log.nextProbConf()\n"+tab
        prog+="return log" 
        return prog

    def valid(self):
        return self.logger.valid() and self.evalExist() and self.lastExist()

    def altMutate(self):
        x = self.duplicate()
        t = None
        while not t:
            n =x.randomNode()
            t = n.params
        n.randomize(x.state)
        
        return x

    def evalExist(self):
        ns =[]
        popNodes(self.root,ns)
        found = False

        for n in ns:
            if n.name =="evaluate":
                found = True
                break
        return found

    def lastExist(self):
        ns =[]
        popNodes(self.root,ns)
        found = False

        for n in ns:
            if n.name =="last" or n.name =='randInd':
                found = True
                break
        return found

    def duplicate(self):
        x = copy.deepcopy(self)
        
        x.aveOps = 0.0
        x.aveBest = 0.0
        x.aveEval = 0.0

        global id
        x.name="bbsa-"+str(id)
        id+=1
        
        x.logger = logger.logger(x.name,self.settings.bbsaSettings['converge'])

        x.state.reset()
        x.state.settings = x.settings
        x.fitness = 0
        x.update()
        return x

    def mutate(self):
        x = self.duplicate()
        n = x.randomNode()
        
        while not n.down:
            n = x.randomNode()
        x.createRandom(n)
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
                    raw_input("hmmm")
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
        s = self.fitness - self.settings.bbsaSettings['penalty']*self.size
        o = other.fitness - self.settings.bbsaSettings['penalty']*other.size

        return s>o

    def dominate(self,other):
        """if self.fitness>=other.fitness and self.size<=other.size and self.aveEval<other.aveEval:
            return True
        if self.fitness>=other.fitness and self.size<other.size and self.aveEval<=other.aveEval:
            return True
        if self.fitness>=other.fitness and self.size<=other.size and self.aveEval<other.aveEval:
            return True"""
        if self.fitness>=other.fitness and self.aveEval<other.aveEval:
            return True
        if self.fitness>other.fitness and self.aveEval<=other.aveEval:
            return True
        
        
        
        return False

    def plot(self):
        self.logger.plot()

    def makeGraph(self):
        val = 'x'
        s = 'strict digraph {\nordering=out;\n  node[label=\"\\N\"];\n '
        s += getEdge(self.root,val)
        s+="\n}"
        f = open(self.name+'.dot','w')
        f.write(s)
        f.close()
        subprocess.call(['dot','-Tpng',self.name+'.dot','-o',self.name+'.png']) 
        
        return

def getEdge(node,val):
    s = ""
    if not node.parent:
        s+= val+" [color=goldenrod2,\n  label =\""+node.toStr()+"\",\n  style=filled];\n"
        #G.add_node(val,label=node.toStr(),color = 'goldenrod2',style='filled')
    
    for i in xrange(len(node.down)): 
        s+= val+str(i+1)+"   [color=goldenrod2,\n  label =\""+node.down[i].toStr()+"\",\n  style=filled];\n"
        #G.add_node(val+str(i+1),label=node.down[i].toStr(),color='goldenrod2',style='filled')
        s+="  "+val+" -> "+val+str(i+1)+';\n'
        #G.add_edge(val,val+str(i+1))
        s+= getEdge(node.down[i],val+str(i+1))
    return s
