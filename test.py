import bbsa
import settings

s = settings.runSettings()

x = bbsa.bbsa(s)

print x.toDict() 
