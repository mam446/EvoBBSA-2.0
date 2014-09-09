import bbsa
import settings
import fitness


#x = fitness.kmeansClassify({'name':'temp.txt','k':2})

#print x.evaluate([1 for i in xrange(256)])



s = settings.runSettings()

x = bbsa.bbsa(s)
x.evaluate()
x.makeGraph()
x.plot()
print x.toDict()

y = bbsa.bbsa(s)
y.load(x.toDict())
print y.toDict()
