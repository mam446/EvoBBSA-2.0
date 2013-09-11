


class test:
    def __init__(self,x,y):
        self.x =x
        self.y = y

    def dominate(self,other):
        if self.x>=other.x and self.y>other.y:
            return True
        if self.x>other.x and self.y>=other.y:
            return True
        return False






class pareto:
    def __init__(self):
        self.top = None
        self.bottom = None

        self.numFronts = 0

    def push(self,obj):
        if not self.top:
            self.top = {'up':None,'down':None,'data':[obj]}
            self.bottom = self.top
            self.numFronts = 1
            return
        cur = self.top
        up = False
        down = True
        while down:
            down = False

            where = self.checkFront(cur['data'],obj)
            if where==1:
                up=True
            elif where==-1:
                down=True
                if not cur['down']:
                    break
                else:
                    cur = cur['down']

        if up:
            self.numFronts+=1
            if not cur['up']:
                cur['up'] = {'up':None,'down':cur,'data':[obj]}
                self.top = cur['up']
            else:
                temp = cur['up']
                cur['up'] = {'up':temp,'down':cur,'data':[obj]}
                temp['down'] = cur['up']
        elif down:
            self.numFronts+=1
            if not cur['down']:
                cur['down'] = {'up':cur,'down':None,'data':[obj]}
                self.bottom = cur['down']
            else:
                temp = cur['down']
                cur['down'] = {'up':cur,'down':temp,'data':[obj]}
                temp['up'] = cur['down']
        else:
            cur['data'].append(obj)


    def checkFront(self,cur,obj):
        val = None

        for i in xrange(len(cur)):
            if cur[i].dominate(obj):
                val = -1
                break
            if obj.dominate(cur[i]):
                val = 1
                break

        if not val:
            return 0
        return val


















