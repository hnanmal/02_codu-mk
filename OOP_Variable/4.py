class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
    def getValue(self):
        return self.__value
    def setValue(self, v):
        self.__value = v

c1 = C(10)
# print(c1.getValue())
c1.setValue(20)
print(c1.getValue())
## print(c1.__value)
# c1.show()