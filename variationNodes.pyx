# cython: profile=True
import random
import genNode
import funcs
import copy
import bitStringVariation
import realValuedVariation
import lSatVariation

single = {'bitString':{'generic':bitStringVariation.single},'realValued':{'generic':realValuedVariation.single}}
multi = {'bitString':{'generic':bitStringVariation.multi},'realValued':{'generic':realValuedVariation.multi}}

single['bitString']['lSat'] = lSatVariation.single
multi['bitString']['lSat'] = lSatVariation.multi


