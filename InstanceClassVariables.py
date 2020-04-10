class DemoVariables:
    num = 1000

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

    def calculator(self):
        return self.firstnumber+self.secondnumber

obj = DemoVariables(2, 3)
obj1 = DemoVariables(4, 5)
print(obj.calculator())
print(obj1.calculator())

