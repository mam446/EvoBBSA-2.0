from mpi4py import MPI
import Queue
import threading
import time
import cPickle
import sys

def childProc():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    while True:
        print "wait receive", rank
        try:
            cur = comm.recv(source = 0,tag = rank)
        except cPickle.UnpicklingError as e:
            print "\t\t",e,ord(str(e)[-3])
            print "\t\tI think it messed up",rank
            comm.send(rank,dest=0)
            continue 
        except:
            print "\t\t\t I messed up again I think",rank
            comm.send(rank,dest=0)
            continue 
        print "received", rank
        time.sleep(.1)
        if cur =="-1":
            if rank ==1:
                comm.send("End",dest=0)
            break
        cur.evaluate()
        comm.send(cur,dest = 0)
        time.sleep(.1)

class processManager:
    def __init__(self):
        self.count = 0
        self.comm = MPI.COMM_WORLD
        self.numNodes = self.comm.Get_size()-1
        
        self.inChildren = Queue.Queue()
        self.outChildren = Queue.Queue()
        
        self.stop = False
        self.stopLock = threading.Lock()


        self.sendLock = threading.Lock()
     
        self.thread = threading.Thread(None,self.respond)
        self.thread.start()


        self.log = [None for i in xrange(self.numNodes)]

        self.logLock = threading.Lock()

    def wait(self,size,timeout=10000000000):
        cur = 0
        while self.outChildren.qsize()<size:
            time.sleep(1)
            cur+=1
            if cur>timeout:
                break

    def add(self,p):
        self.inChildren.put(p)

    def getPop(self):
        l = self.outChildren.qsize()
        return [self.outChildren.get() for i in xrange(l)]
        

    def start(self):
        for i in xrange(self.numNodes):
            self.sendLock.acquire()
            cur = self.inChildren.get()

            self.logLock.acquire()
            self.log[i] = cur
            self.logLock.release()
            print "start send",i
            time.sleep(.1)
            self.comm.isend(obj = cur,dest = i+1,tag = i+1)
            self.sendLock.release()
            time.sleep(.1)
            print "stop send",i

    def kill(self):
        for i in xrange(self.numNodes):
            self.comm.send(obj="-1",dest = i+1,tag = i+1)


    def respond(self):
        while True:
            stat = MPI.Status()
            resp = self.comm.recv(source = MPI.ANY_SOURCE,status=stat)
            time.sleep(.1)
            if type(resp) is int:
                print "fixing it"
                self.logLock.acquire()
                ret = self.log[resp-1]
                print ret, "from", stat.Get_source()
                print self.log
                self.logLock.release()

                self.sendLock.acquire()
                self.comm.send(ret,dest=resp,tag=resp)
                self.sendLock.release()
                continue
            else:
                print self.log[stat.Get_source()-1]
            if resp=="End":
                return
            
            self.outChildren.put(resp)
            print self.outChildren.qsize(),stat.Get_source()
            if not self.inChildren.empty():
                self.sendLock.acquire()
                ret = self.inChildren.get()

                self.logLock.acquire()
                self.log[stat.Get_source()-1] = ret
                self.logLock.release()

                self.comm.send(ret,dest=stat.Get_source(),tag = stat.Get_source())
                self.sendLock.release()
            
                 
            self.stopLock.acquire()
            if self.stop:
                self.stopLock.release()
                break
            self.stopLock.release()
            time.sleep(.1)






