import settings
import logger
import sys

def externalRun(settingsFile =None):


    plugName = sys.argv[1]
    name = plugName[:-3]
    if not settingsFile:
        if len(sys.argv)<2:
            raise "Must supply settings file"
        settingsFile = sys.argv[2]
    s = settings.runSettings(settingsFile)

    solSettings = s.probConf


    plug = __import__(plugName) 
    log = logger.logger(name,0)
    j = 0


    labels = []
    for l in s.probConf:
        k = ""
        for key in l['settings']: 
            k+=key+"="+str(l['settings'][key])+", "

        labels.append(k)

    for d in solSettings:
        log = plug.run(int(sys.argv[3]),log,d,name,j)
        j+=1


    log.log()
    log.plot(labels)


if __name__ =="__main__":
    externalRun()

