# cython: profile=True
from random import random
#goldman's implementations
import FitnessFunction

#my implementations
import fitness

from itertools import repeat

def createBitstring(settings):
    cdef int i
    return [int(random()*2) for i in xrange(settings['length'])]

def createRealValued(settings):
    cdef int i
    return [random()*2-1 for i in xrange(settings['vars'])]

def testFitnessFunction(settings):
    return fitness.testFit(settings)

def allOnesFitnessFunction(settings):
    return fitness.allOnes(settings)

def dTrapFitnessFunction(settings):
    return FitnessFunction.DeceptiveTrap(settings)

def dStepTrapFitnessFunction(settings):
    return FitnessFunction.DeceptiveStepTrap(settings)


def nkFitnessFunction(settings):
    return FitnessFunction.NearestNeighborNK(settings,settings['run'])

def allOnes(settings):
    return fitness.allOnes(settings)    

reps = {}
reps['bitString'] = {'gene':createBitstring}
reps['bitString']['dTrap'] = dTrapFitnessFunction
reps['bitString']['dSTrap'] = dStepTrapFitnessFunction
reps['bitString']['nk'] = nkFitnessFunction
reps['bitString']['allOnes'] = allOnesFitnessFunction

reps['realValued'] = {'gene':createRealValued}
reps['realValued']['test'] = testFitnessFunction










