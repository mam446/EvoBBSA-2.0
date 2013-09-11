import bbsa
import settings

s = settings.runSettings()

x = bbsa.bbsa(s)
y = bbsa.bbsa(s)

(z1,z2) = x.mate(y)
print x.toDict()
print
print y.toDict()
print 
print z1.toDict()
#x.evaluate()

print len(x.logger.probConf)
#print x.fitness
#f = open(str(x.name)+"allones.py","w")
#f.write(x.makeProg())
#f.close()
