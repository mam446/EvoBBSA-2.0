#cython: profile=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random





class logger:
    def __init__(self,name,converge):
        
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.probOps = []
        self.ops = []
        self.name = name
        
        self.curMax = 0
        self.aveMax = 0

        self.converge = converge
        self.allMax = None        
        self.curCon = 0
        self.conVal = 0.0
        self.count = 0

        self.probExec = []
        self.runsExec = []
        self.curExec = []


    def reset(self):
        self.probConf = []
        self.runs = []
        self.curRun = []
        self.probOps = [] 
        self.ops = []
        self.aveMax = 0    
        self.allMax = None

        self.curCon = 0
        self.conVal = 0.0
        self.count = 0

    def nextRun(self):
        self.runs.append(self.curRun)
        self.runsExec.append(self.curExec)
        self.curExec = []
        self.curRun = []
        self.curCon = 0
        self.conVal = 0.0
        self.allMax = None
        self.aveMax +=self.curMax
        self.count+=1
        self.curMax = 0


    def nextProbConf(self):
        self.probConf.append(self.runs)
        self.probExec.append(self.runsExec)
        self.runsExec = []
        self.runs = []
        self.probOps.append(self.ops)
        self.ops = []
        self.curCon = 0
        self.conVal = 0.0
        self.allMax = None
        self.curMax = 0

    def nextIter(self,state):
        gMax = None
        Sum = 0.0
        num = 0
        popSize = 0
        for d in state.pers:
            popSize+= len(state.pers[d])
            for ind in state.pers[d]:
                if not gMax or ind.fitness>gMax.fitness:
                    gMax = ind
                Sum+=ind.fitness
                num+=1
        popSize+=len(state.last)
        for ind in state.last:
            if not gMax or ind.fitness>gMax.fitness:
                gMax = ind
            Sum+=ind.fitness
            num+=1
        if num:
            ave = Sum/num
        else:
            ave = 0
        if gMax and self.allMax!=None and gMax.fitness<=self.allMax.fitness or popSize==0:
            self.curCon+=1
        else:
            self.curCon = 0
            if gMax:
                self.allMax = gMax
        if gMax:
            self.curRun.append({'evals':state.curEval,'max':gMax.fitness,'ave':ave,'popSize':popSize})
        else:
            self.curRun.append({'evals':state.curEval,'max':0,'ave':ave,'popSize':popSize})
        if gMax and gMax.fitness>self.curMax:
            self.curMax = gMax.fitness
            self.curCon = 0 
        self.ops.append(state.curOp)

    def countConverged(self):
        return self.curCon

    def changedExec(self,state):
        self.curExec.append(state.curEval)
        

    def hasConverged(self):
        if self.curMax==1.0:
            return True
        return self.curCon>=self.converge

    def getFitness(self):
        if self.aveMax>1:
            self.aveMax/=float(self.count)
        return self.aveMax

    def getAveOps(self):
        Sum = 0.0
        num = 0
        for p in self.probOps:
            for r in p:
                Sum+=r
                num+=1
        return Sum/num


    def valid(self):
        
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                if len(r)-1:
                    Sum+=r[-1]['max']
                num+=1

        if (Sum<.001 and Sum>-.001) or num==0:
            return False 
        return True

    def getAveBest(self):
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['max']
                num+=1
        return Sum/num
    
    def getFullSpan(self):
        mi=None
        ma=None

        for p in self.probConf:
            for r in p:
                if not mi or mi>r[-1]['max']:
                    mi = r[-1]['max']

                if not ma or ma<r[-1]['max']:
                    ma = r[-1]['max']

        return ma-mi
    
    def getSpan(self):
        Sum = 0.0
        num=0
        l = []
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['max']
                num+=1
            l.append( Sum/num)
            Sum = 0.0
            num = 0
        return max(l)-min(l)
    def getAveEvals(self):
        Sum = 0.0
        num=0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['evals']
                num+=1
        return Sum/num
   
    def getAveAve(self):
        Sum = 0.0
        num = 0.0
        for p in self.probConf:
            for r in p:
                Sum+=r[-1]['ave']
                num+=1
        return Sum/num
     
    def log(self):
        for i in xrange(len(self.probConf)):
            f = open(self.name+"-"+str(i),'w')
            r = ""
            for x in xrange(len(self.probConf[i])):
                r+=str(x)+"\t"
            w = 'evals\t'+r+"\n"
            
            fm = ""
            fm+=w
            #print len(self.probConf[i])
            for j in xrange(len(self.probConf[i][0])):
                line = ""
                for k in xrange(len(self.probConf[i])):
                    if k==0:
                        line+=str(self.probConf[i][k][j]['evals'])+'\t'
                    if i<len(self.probConf[i][k]):
                        try:
                            line+=str(self.probConf[i][k][j]['max'])+'\t'
                        except:
                            line+="NULL"+'\t'
                    else:
                        line+='\t'
                line+='\n'
                fm+=line
            f.write(fm)
            f.close()
                        
        return

    def plot(self,labels = None):
        #max Plot

        x = []
        y = []
        
        psy = []
        
        for prob in self.probConf:
            psyi = [0.0]

            xi = [0.0]
            yi = [0.0]
            ci = [1]
            first = True
            for run in prob:
                for it in xrange(len(run)):
                    if first:
                        psyi.append(run[it]['popSize'])
                        xi.append(run[it]['evals'])
                        yi.append(run[it]['max'])
                        ci.append(1)
                    else:
                        """if len(yi)>it:
                            if len(run)>it:
                                yi[it]+=run[it]['max']
                                psyi[it]+=run[it]['popSize']
                                ci[it]+=1
                            else:
                                yi[it]+=run[-1]['max']
                                psyi[it]+=run[-1]['popSize']
                                ci[it]+=1
                        else:
                            if len(run)>it:
                                psyi.append(run[it]['popSize'])
                                xi.append(run[it]['evals'])
                                yi.append(run[it]['max'])
                                ci.append(1)
                            else:
                                psyi.append(run[-1]['popSize'])
                                xi.append(run[-1]['evals'])
                                yi.append(run[-1]['max'])
                                ci.append(1)
                        """
                        try: 
                            yi[it]+=run[it]['max']
                            psyi[it]+=run[it]['popSize']
                            ci[it]+=1
                        except IndexError:
                            psyi.append(run[it]['popSize'])
                            xi.append(run[it]['evals'])
                            yi.append(run[it]['max'])
                            ci.append(1)
                            #print it,len(yi),len(run)"""
                first = False
            for d in xrange(len(yi)):
                yi[d]/=ci[d]
            for d in xrange(len(psyi)):
                psyi[d]/=ci[d]
            psy.append(psyi)
            x.append(xi)
            y.append(yi)
        cm = plt.get_cmap('gist_rainbow')
        ax =  plt.subplot(1,1,1)
        ax.set_position([.1,.1,.7,.8])
        color = [cm(1.*i/len(y)) for i in xrange(len(y))]
        ax.set_color_cycle(color)
        ax.set_ylim([.2,1.0])
        d = 0
        for pc in self.probExec:
           
            for r in pc:
                for e in r:
                    ax.axvline(x=e,linewidth=.5,c = color[d])
            d+=1
        if x:
            ax.set_xlim([0,x[0][-1]])
        for d in xrange(len(x)):
            #print len(x[d]),len(y[d])
            if labels:
                ax.plot(x[d],y[d],label = labels[d])
            else:
                ax.plot(x[d],y[d],label = str(d))
                         
        lgd = ax.legend(bbox_to_anchor=(.5,-0.1), loc='upper center',borderaxespad=0)
        """ax2 = plt.subplot(1,2,2)
        color = [cm(1.*i/len(y)) for i in xrange(len(y))]
        #ax2.set_color_cycle(color)
        if x:
            ax2.set_xlim([0,x[0][-1]])
        for d in xrange(len(x)):
            #print len(x[d]),len(y[d])
            if labels:
                ax2.plot(x[d],psy[d],label = labels[d])
            else:
                ax2.plot(x[d],psy[d],label = str(d))
        """

        try:
            plt.savefig(self.name+'-plot-l.png',bbox_extra_artists=(lgd,),bbox_inches='tight')
        except:
            print "That didn't work"
        plt.savefig(self.name+'-plot.png')
        plt.clf()
        return



    def compare(self,other,name1,name2,labels = None):
        #max Plot

        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for prob in self.probConf:
            xi = []
            yi = []
            ci = []
            first = True
            for run in prob:
                for it in xrange(len(run)):
                    if first:
                        xi.append(run[it]['evals'])
                    if first:
                        yi.append(run[it]['max'])
                        ci.append(1)
                    else:
                        try:
                            yi[it]+=run[it]['max']
                            ci[it]+=1
                        except:
                            xi.append(run[it]['evals'])
                            yi.append(run[it]['max'])
                            ci.append(1)
                            #print it,len(yi),len(run)
                first = False
            for d in xrange(len(yi)):
                yi[d]/=ci[d]

            x1.append(xi)
            y1.append(yi)


        for prob in other.probConf:
            xi = []
            yi = []
            ci = []
            first = True
            for run in prob:
                for it in xrange(len(run)):
                    if first:
                        xi.append(run[it]['evals'])
                    if first:
                        yi.append(run[it]['max'])
                        ci.append(1)
                    else:
                        try:
                            yi[it]+=run[it]['max']
                            ci[it]+=1
                        except:
                            xi.append(run[it]['evals'])
                            yi.append(run[it]['max'])
                            ci.append(1)
                            #print it,len(yi),len(run)
                first = False
            for d in xrange(len(yi)):
                yi[d]/=ci[d]

            x2.append(xi)
            y2.append(yi)


        for p in xrange(len(self.probConf)):

            plt.suptitle(labels[p])
            ax =  plt.subplot(1,1,1)
            ax.set_position([.1,.1,.7,.8])
            ax.set_ylim([.6,1.0])
            ax.set_xlim([0,max([x1[0][-1],x2[0][-1]])])
            ax.plot(x1[p],y1[p],label=name1)
            ax.plot(x2[p],y2[p],label=name2)
            ax.legend(bbox_to_anchor=(1.05,.5), loc='center left',borderaxespad=0)
            plt.savefig(labels[p]+'-.png')
            plt.clf()
        return











