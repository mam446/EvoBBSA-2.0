
#import SGA
#import nsga
import sys
import settings
from subprocess import Popen,PIPE


def extHydra(settingsFile = None):
    s = None
    
    plugNameDir = sys.argv[1]
    plugName = sys.argv[1].split("/")[-1]

    if not settingsFile:
        if len(sys.argv)<2:
            raise "Must supply settings file"
        settingsFile = sys.argv[2]
    s = settings.runSettings(settingsFile)



    t = s.hyperSettings['type']
    mpi = s.hyperSettings['mpi']
    procs = s.hyperSettings['procs']
    runName = s.hyperSettings['runName']
    runNum = s.hyperSettings['runNumber']
    
    if len(sys.argv)>3:
        runNum = int(sys.argv[3])
    runDir = 'externalRuns/'+runName+"/"+str(runNum)

    

    #Setup file locations
    
    #check if experiment dir exists
    lsProc = Popen(['ls','externalRuns/'],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        mkdirProc = Popen(['mkdir','externalRuns/'],stdout=PIPE,stderr=PIPE)

    #check runName dir exists
    lsProc = Popen(['ls','externalRuns/'+runName],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        mkdirProc = Popen(['mkdir','externalRuns/'+runName],stdout=PIPE,stderr=PIPE)
    
    #check if run dir exists 
    lsProc = Popen(['ls','externalRuns/'+runName+"/"+str(runNum)],stdout=PIPE,stderr=PIPE)
    stdout,stderr = lsProc.communicate()
    if lsProc.returncode!=0:
        lsProc = Popen(['mkdir','externalRuns/'+runName+"/"+str(runNum)],stdout=PIPE,stderr=PIPE)
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

    cpProc = Popen(['cp',settingsFile,runDir],stdout=PIPE,stderr=PIPE)
    cpProc.communicate()
    
    cpProc = Popen(['cp',plugNameDir,'.'],stdout=PIPE,stderr=PIPE)
    cpProc.communicate()
    
    for r in s.probConf:
        if 'name' in r['settings']:
            cpProc = Popen(['cp',r['settings']['name'],runDir],stdout=PIPE,stderr=PIPE)
            cpProc.communicate()
            if cpProc.returncode!=0:
                print "Cannot find file",r['settings']['name']
                return 

    settingsFile = settingsFile.split("/")[-1]
    loc = plugNameDir.replace('/','.')
    print loc
    loc = 'externalRuns'+loc[11:]
    print loc
    if plugName[-2:] == 'py':
        plugName = plugName[:-3]
    runProc = Popen(['python','../../../run.py',plugName,settingsFile,"30"],cwd=runDir)
    runProc.communicate()
    
    cpProc = Popen(['mv',plugNameDir,runDir],stdout=PIPE,stderr=PIPE)
    cpProc.communicate()


if __name__ =="__main__":
    extHydra()



