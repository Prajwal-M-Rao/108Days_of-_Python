#Type3: Method that takes parameter gives a no return value
#takes arguments doesn't but returns a value
class Calculator:
    def __init__(self):
        self.x=20
        self.y=25

    def Disp(self,a,b):
        c=a+b
        print(c)
c=Calculator()
c.Disp(10,12)

#Type3: Method that takes parameter gives a return value
#takes arguments and returns a value
class Calculator:
    def __init__(self):
        self.x=20
        self.y=25

    def Disp(self,a,b):
        c=a+b
        return c
c=Calculator()
p1=c.Disp(50,15)
print(p1)