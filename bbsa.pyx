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

nodes = {'bitString':{},'realValued':{}}
single = {'bitString':{},'realValued':{}}
multi = {'bitString':{},'realValued':{}}
global id
id = 0

#nodes.extend(variationNodes.nodes)
#nodes.extend(selectNodes.nodes)
#nodes.extend(evalNodes.nodes)
#nodes.extend(setNodes.nodes)

terms = termNodes.multi

probSpecSingle = {'bitString':{},'realValued':{}}
probSpecMulti = {'bitString':{},'realValued':{}}

probSpecSingle['bitString']['lSat'] = variationNodes.single['bitString']['lSat']
probSpecMulti['bitString']['lSat'] = variationNodes.multi['bitString']['lSat']

single['bitString'].update(variationNodes.single['bitString']['generic'])
single['bitString'].update(selectNodes.single['bitString'])
single['bitString'].update(evalNodes.single['bitString'])
single['bitString'].update(setNodes.single['bitString'])
single['bitString'].update(auxNodes.single['bitString'])

single['realValued'].update(variationNodes.single['realValued']['generic'])
single['realValued'].update(selectNodes.single['realValued'])
single['realValued'].update(evalNodes.single['realValued'])
single['realValued'].update(setNodes.single['realValued'])
single['realValued'].update(auxNodes.single['realValued'])

multi['bitString'].update(variationNodes.multi['bitString']['generic'])
multi['bitString'].update(selectNodes.multi['bitString'])
multi['bitString'].update(evalNodes.multi['bitString'])
multi['bitString'].update(setNodes.multi['bitString'])
multi['bitString'].update(auxNodes.multi['bitString'])

multi['realValued'].update(variationNodes.multi['realValued']['generic'])
multi['realValued'].update(selectNodes.multi['realValued'])
multi['realValued'].update(evalNodes.multi['realValued'])
multi['realValued'].update(setNodes.multi['realValued'])
multi['realValued'].update(auxNodes.multi['realValued'])


def popNodes(node,a):
    a.append(node)
    for x in node.down:
        popNodes(x,a)


class bbsa:
    
    def __init__(self,settings):
        self.time = 0
        self.root = None

        self.depth = 0
        self.size = 0
       
        self.curObjectives = ['fitness','evals','time']
        
        self.objectives = {}
        self.objectives['fitness'] = {'value':0,'op':'max'}
        self.objectives['evals'] = {'value':0,'op':'min'}
        self.objectives['time'] = {'value':0,'op':'min'}

        global id
        self.name="bbsa-"+str(id)
        id+=1
        self.grow = False

        self.aveOps = 0.0
        self.aveBest = 0.0
        self.aveEval = 0.0

        self.fitness = 0.0

        self.settings = settings

        self.state = state.state(settings)

        self.initPop = random.randint(1,settings.bbsaSettings['initPopMax'])
        
        self.logger = logger.logger(self.name,settings.bbsaSettings['converge'])
         
        self.useMulti = multi[self.settings.bbsaSettings['representation']].keys()
        self.useSingle = single[self.settings.bbsaSettings['representation']].keys()
        if self.settings.bbsaSettings['problem'] in probSpecMulti[self.settings.bbsaSettings['representation']]:
            self.useMulti.extend(probSpecMulti[self.settings.bbsaSettings['representation']][self.settings.bbsaSettings['problem']])
            self.useSingle.extend(probSpecSingle[self.settings.bbsaSettings['representation']][self.settings.bbsaSettings['problem']])


        self.curObjectives = self.settings.hyperSettings['objectives']

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
                node = multi[self.settings.bbsaSettings['representation']][random.choice(self.useMulti)]
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
            if cur.take[n]==2:
                node = multi[self.settings.bbsaSettings['representation']][random.choice(self.useMulti)]
                cur.down[n] = node(cur,self.settings)
                
                cur.down[n].setTake(max(cur.down[n].canTake))
                cur.down[n].randomize(self.state)
            else:
                node = single[self.settings.bbsaSettings['representation']][random.choice(self.useSingle)]
                cur.down[n] = node(cur,self.settings)
                cur.down[n].setTake(1)
                cur.down[n].randomize(self.state)

        start.fillTerms(self.state)
        if self.root == None:
            self.root = start
        self.update()
        self.count()
        return


    def load(self,b,parent=None,child= 0):
        if b is str:
            b = eval(b)
        [key] = b.keys() 
        parts = key.split("(")
        name = parts[0]
        if len(parts)>1:
            params = parts[1][:-1]
            params = params.split(",")
        else:
            params = []
        node = None
        if name in multi[self.settings.bbsaSettings['representation']]:
            node = multi[self.settings.bbsaSettings['representation']][name](parent,self.settings)
        elif name in single[self.settings.bbsaSettings['representation']]:
            node = single[self.settings.bbsaSettings['representation']][name](parent,self.settings)
        elif name in terms:
            node = terms[name](parent,self.settings)
        else:
            if len(key) ==1:
                node = terms['termNode'](parent,self.settings)
                node.name = key
            else:
                print key
                raise "Cannot load program"
        if not parent:
            node.setTake(max(node.canTake))
        elif parent.take[child]==2:
            node.setTake(max(node.canTake))
        else:
            node.setTake(1)
        #load parameters
        for p in params:
            x = p.split("=")

            try:
                node.params[x[0]]['value'] = eval(x[1])
            except(NameError):
                node.params[x[0]]['value'] = str(x[1])

        if not parent:
            self.root = node    
        else:
            parent.down[child] = node
        for i in xrange(len(b[key])):
            self.load(b[key][i],node,i)
        if not parent:
            self.update()
            self.count()


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
                check = time.time()
                if check-start>self.settings.bbsaSettings['time'] or self.grow:
                    self.fitness = -1 
                    return
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
        self.fitness = self.logger.getFitness()
        end = time.time()
        st = ""
        self.time = end-start
        
        #v = self.vectorize()
        #for item in v:
        #    st+=str(item)+", "
        
        if end-start>self.settings.bbsaSettings['time']:
            t = self.name
            self.name +="-long"+str(int(end-start))
            self.makeGraph()
            self.plot()
            self.name = t

    def run(self):
        self.state.last = [solution.solution(self.settings.solSettings) for i in xrange(self.initPop)]
        prev = -1
        for it in xrange(self.settings.bbsaSettings['maxIterations']):
            self.state.last = self.root.evaluate()
            self.logger.nextIter(self.state)
            size = 0
            size+=len(self.state.last)
            pre = size
            #print "\t\tpopSize:",size
            for s in self.state.pers:
                size+=len(self.state.pers[s])
            #print "\t\ttotSize:",size
            if self.state.done() or self.logger.hasConverged():
                break
            if prev>=0:
                if size>prev:
                    self.grow = True
                else:
                    self.grow = False
            prev = size
        self.state.lastEval()
        self.logger.nextIter(self.state)
 
    def randomNode(self,inc=False):
        z = []
        if inc:
            z.append("pop")
        popNodes(self.root,z)
        n = random.choice(z)
        return n

    def count(self):
        self.size = self.root.count()

    def update(self):
        self.state.logger = self.logger
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
            n =x.randomNode(True)
            if n=="pop":
                break
            t = n.params
        if n=="pop":
            self.initPop = random.randint(1,self.settings.bbsaSettings['initPopMax'])
        else:
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
        x.fitness = 0.0
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
        if self.fitness==1 and other.fitness==1:
            return self.aveEvals<other.aveEvals
        s = self.fitness - self.settings.bbsaSettings['penalty']*(self.time)
        o = other.fitness - self.settings.bbsaSettings['penalty']*(other.time)

        return s>o

    def dominate(self,other):
        """if self.fitness>=other.fitness and self.size<=other.size and self.aveEval<other.aveEval:
            return True
        if self.fitness>=other.fitness and self.size<other.size and self.aveEval<=other.aveEval:
            return True
        if self.fitness>=other.fitness and self.size<=other.size and self.aveEval<other.aveEval:
            return True"""
        if self.fitness>=other.fitness and self.time<other.time:
            return True
        if self.fitness>other.fitness and self.time<=other.time:
            return True
        return False


    def calcDistance(self,other):
        return ((self.fitness-other.fitness)**2+(self.time-other.time)**2)**.5


    def plot(self):
        labels = []
        for l in self.settings.probConf:
            s = ""
            for key in l['settings']: 
                s+=key+"="+str(l['settings'][key])+", "

            labels.append(s)
        self.logger.plot(labels)

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
