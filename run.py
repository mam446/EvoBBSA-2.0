import logger
import sys


plug = __import__(sys.argv[1]) 
log = logger.logger(sys.argv[3],0)
solSettings = []
solSettings.append({'settings': {'length': 100, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 200, 'k': 5}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 105, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

solSettings.append({'settings': {'length': 210, 'k': 7}, 'repr': 'bitString', 'weight': 1, 'prob': 'dTrap'})

for s in solSettings:
    log = plug.run(int(sys.argv[2]),log,s,sys.argv[3])


log.log()

