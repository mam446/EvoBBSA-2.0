import logger
import sys


plug = __import__(sys.argv[1]) 
plug2= __import__(sys.argv[2])
log = logger.logger(sys.argv[1],0)
log2 = logger.logger(sys.argv[2],0)
solSettings = []
j = 0

solSettings.append({'settings': {'length': 100, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 105, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 200, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})


solSettings.append({'settings': {'length': 210, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 300, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 99, 'k': 9}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 198, 'k': 9}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 150, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 250, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 147, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 252, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
#solSettings.append({'settings': {'nkProblemFolder': './', 'run': 0, 'dimensions': 30, 'k': 5, 'length': 100, 'problemSeed': 0}, 'repr': 'bitString', 'weight': 1, 'prob': 'nk'})
#solSettings.append({'settings': {'nkProblemFolder': './', 'run': 0, 'dimensions': 30, 'k': 7, 'length': 100, 'problemSeed': 0}, 'repr': 'bitString', 'weight': 1, 'prob': 'nk'})
#solSettings.append({'settings': {'length': 216, 'name': 'test4.cnf'}, 'prob': 'lSat', 'weight': 1, 'repr': 'bitString'})
#solSettings.append({'settings': {'length': 343, 'name': 'test5.cnf'}, 'prob': 'lSat', 'weight': 1, 'repr': 'bitString'})

labels = []
for l in solSettings:
    labels.append(str(l['settings']['length'])+","+str(l['settings']['k']))


for s in solSettings:
    log = plug.run(int(sys.argv[3]),log,s,sys.argv[1],j)
    j+=1

for s in solSettings:
    log2 = plug2.run(int(sys.argv[3]),log2,s,sys.argv[2],j)
    j+=1

log.log()
log2.log()
log.plot(labels)
log2.plot(labels)

log.compare(log2,sys.argv[1],sys.argv[2],labels)

print 
print "Average",log.getAveBest()
print "Span:",log.getSpan()
print "Full Span",log.getFullSpan()

solSettings.append({'settings': {'length': 100, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 400, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 800, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 1000, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 420, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 840, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 1050, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

