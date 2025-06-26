class Demo:
    x = 10  # Class variable

    def __init__(self):
        self.y = 100  # Instance variable
        self.x = 200  # Shadows class variable x

    def instanceDisp(self):
        print(self.y)
        print(self.x)

    @staticmethod
    def staticDisp():
        print(Demo.x)

    @classmethod
    def classDisp(cls):
        print("Python")

d1 = Demo()
d1.instanceDisp()
Demo.staticDisp()
Demo.classDisp()
