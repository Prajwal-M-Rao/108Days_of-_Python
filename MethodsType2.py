#Type2: Method that takes no parameter but gives a return value
#Doesn’t take arguments but returns a value
class Calculator:
    def __init__(self):
        self.x=20
        self.y=25

    def Disp(self):
        a=int(10)
        b=int(35)
        c=a+b
        return c
c=Calculator()
ref=c.Disp()
print(ref)
#Even though the value is same as previous one but here there is a return value
