from InstanceClassVariables import DemoVariables



class DemoInheritance(DemoVariables):
    num1 = 800

    def __init__(self):
        DemoVariables.__init__(self, 1, 2)

    def summation(self):
        return self.num1 + self.calculator()


obj2 = DemoInheritance()
print(obj2.summation())