#Type1: Method that takes no parameter and doesnotgive any return value
#This type of function neither takes arguments nor returns a value. It just executes some statements.
class Calculator:
    def __init__(self):
        self.x=20
        self.y=25

    def Disp(self):
        a=int(10)
        b=int(35)
        c=a+b
        print(c)
c=Calculator()
c.Disp()
