


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






class topFront:
    def __init__(self):
        self.top = []

    def push(self,obj):
        remove = []
        for i in xrange(len(self.top)):
            if self.top[i].dominate(obj):
                return
            if obj.dominate(self.top[i]):
                remove.append(self.top[i])
        for i in xrange(len(remove)):
            self.top.remove(remove[i])
        self.top.append(obj)
                













