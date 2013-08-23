import bbsa
import settings

s = settings.runSettings()

x = bbsa.bbsa(s)

print x.toDict() 

x.evaluate()

print len(x.logger.probConf)

