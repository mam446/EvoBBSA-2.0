import bbsa
import settings

s = settings.runSettings()

x = bbsa.bbsa(s)

x.makeGraph()
f = open('asdfasdf.py','w')
f.write(x.makeProg())
f.close()
print x.toDict()
