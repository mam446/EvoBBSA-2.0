import bbsa
import settings

s = settings.runSettings()

x = bbsa.bbsa(s)

print x.toDict() 

#x.evaluate()

print len(x.logger.probConf)
print x.fitness
f = open(str(x.name)+"allones.py","w")
f.write(x.makeProg())
f.close()
