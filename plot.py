import logger
import sys


plug = __import__(sys.argv[1]) 
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

maxK = 20
minK = 4
minN = 75
maxN = 300

d = [76,75,78,77,80,81,80,77,72,78,70,75,80,68,72,76,80]
a = 0

f = open(sys.argv[1]+"-data.dat",'w')
for k in xrange(minK,maxK):
    n = d[a]
    while n<maxN:
        solSettings = []
        solSettings.append({'settings': {'length': n, 'k': k}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
        
        log = logger.logger(sys.argv[1],0)
        log = plug.run(int(sys.argv[2]),log,solSettings[0],sys.argv[1],0)
        f.write(str(k)+", "+str(n)+", "+str(log.getAveBest())+"\n")
        print k,n,log.getAveBest()       
        n+=k
    a+=1
f.close()

solSettings.append({'settings': {'length': 100, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 400, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 800, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 1000, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 420, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 840, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})
solSettings.append({'settings': {'length': 1050, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

