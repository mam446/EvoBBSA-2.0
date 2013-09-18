import logger
import sys


plug = __import__(sys.argv[1]) 
log = logger.logger(sys.argv[3],0)
 



log = plug.run(int(sys.argv[2]),log)



