import bbsa
import settings
import fitness


#x = fitness.kmeansClassify({'name':'temp.txt','k':2})

#print x.evaluate([1 for i in xrange(256)])



s = settings.runSettings()

x = bbsa.bbsa(s)

print x.toDict()
x.makeGraph()

x.evaluate()

x.plot()
#f = open('asdfasdf.py','w')
#f.write(x.makeProg())
#f.close()
