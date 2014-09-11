
#import SGA
#import nsga
import sys
import settings
from subprocess import Popen,PIPE


def runHydra(settingsFile = None):
    s = None
    if not settingsFile:
        if len(sys.argv)<2:
            raise "Must supply settings file"
        settingsFile = sys.argv[1]
    s = settings.runSettings(settingsFile)



    t = s.hyperSettings['type']
    mpi = s.hyperSettings['mpi']
    procs = s.hyperSettings['procs']
    runName = s.hyperSettings['runName']
    runNum = s.hyperSettings['runNumber']
    
    if len(sys.argv)>2:
        runNum = int(sys.argv[2])
    runDir = 'experiments/'+runName+"/"+str(runNum)

    

    #Setup file locations
    
    #check if experiment dir exists
    lsProc = Popen(['ls','experiments/'],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        mkdirProc = Popen(['mkdir','experiments/'],stdout=PIPE,stderr=PIPE)

    #check runName dir exists
    lsProc = Popen(['ls','experiments/'+runName],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        mkdirProc = Popen(['mkdir','experiments/'+runName],stdout=PIPE,stderr=PIPE)
    
    #check if run dir exists 
    lsProc = Popen(['ls','experiments/'+runName+"/"+str(runNum)],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        lsProc = Popen(['mkdir','experiments/'+runName+"/"+str(runNum)],stdout=PIPE,stderr=PIPE)
    else:
        print "Run Number directory exists. Run may not perform properly"
        choice = raw_input("Continue?(y/n): ")
        if choice=='y' or choice=='Y' or choice =='yes' or choice =='Yes':
            print "Continuing"
        elif choice=='n' or choice=='N' or choice=='no' or choice =='No':
            print "Quitting"
            return        
        else:
            print "Not valid Option"

    lsProc = Popen(['ls','experiments/'+runName+"/"+str(runNum)+"/"+settingsFile],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    
    if lsProc.returncode!=0:
        cpProc = Popen(['cp',settingsFile,runDir],stdout=PIPE,stderr=PIPE)
        cpProc.communicate()
    
    for r in s.probConf:
        if 'name' in r['settings']:
            cpProc = Popen(['cp',r['settings']['name'],runDir],stdout=PIPE,stderr=PIPE)
            cpProc.communicate()
            if cpProc.returncode!=0:
                print "Cannot find file",r['settings']['name']
                return 

    settingsFile = settingsFile.split("/")[-1]


    if mpi:
        #do MPI
        if t=='SGA':
            #SGA
            print "SGA"
            runProc = Popen(['mpiexec','-n',str(procs),'python','../../../mpi-SGA.py',settingsFile],cwd=runDir)
            stdout,stderr = runProc.communicate()
        elif t=='nsga':
            #NSGA
            print "nsga"
            mkProc = Popen(['mkdir',runDir+'/finalFront'],stdout=PIPE,stderr=PIPE)
            stdout,stderr = mkProc.communicate()
            runProc = Popen(['mpiexec','-n',str(procs),'python','../../../mpi-nsga.py',settingsFile],cwd=runDir)
            stdout,stderr = runProc.communicate()
        else:
            raise "Not valid Evolution Type" 

    else:
        #don't do MPI
        if t=='SGA':
            #SGA
            print "SGA"
            runProc = Popen(['python','../../../SGA.py',settingsFile],cwd=runDir)
            stdout,stderr = runProc.communicate()
        elif t=='nsga':
            #NSGA
            print "nsga"
            mkProc = Popen(['mkdir',runDir+'/finalFront'],stdout=PIPE,stderr=PIPE)
            stdout,stderr = mkProc.communicate()
            runProc = Popen(['python','../../../nsga.py',settingsFile],cwd=runDir)
            stdout,stderr = runProc.communicate()
        else:
            raise "Not valid Evolution Type" 


if __name__ =="__main__":
    runHydra()



