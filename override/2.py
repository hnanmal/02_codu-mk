class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2,int):
            self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)


class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2
    
    def info(self):
        return "CalMultiply => %s " % super().info()


class CalDivide(CalMultiply):
    def divide(self):
        return self.v1 / self.v2

    def info(self):
        return "CalDivide => %s " % super().info()

c0 = Cal(30,60)
print(c0.info())
c1 = CalMultiply(10,10)
print(c1.info())
c2 = CalDivide(20,10)
print(c2.info())
#m.Q