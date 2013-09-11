import sys


plug = __import__(sys.argv[1]) 

x = plug.run(numRuns=int(sys.argv[2]))
i=0
print x['settings'].curEvals

for y in x['sets']:
    y.sort(reverse=True)
    
    print "set",i 
    if y:
        print y[0].bits
    for z in  y:
        print z.fitness
    i+=1



