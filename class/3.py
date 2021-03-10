class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
 
    def add(self):
        return self.v1+self.v2
 
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
 
c1 = Cal(10,10)
# print(c1.add())
# print(c1.subtract())
# c2 = Cal(30,20)
# print(c2.add())
# print(c2.subtract())

c1.setV1(50)
print(c1.add())
print(c1.subtract())
print(c1.getV1())