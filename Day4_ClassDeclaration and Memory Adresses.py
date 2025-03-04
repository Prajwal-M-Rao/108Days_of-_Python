#In this we will know how the values are stored and how the variables point to those.
class Fan:
    def __init__(self):
        self.brand="Havels"
        self.color="Peach"
        self.prize=5000
        self.blades=5
        print(self)
f1=Fan()
print(f1)
f2=f1
print(f2)
print(id(f1))
print(id(f2))
print(f1 is f2)
# Even though f1 and f2 are two different objects, In python a value is assigned with a memory space only once, if the same value repeates then, the variable just points to the value.
# There no creation/allocation of memory for the repeated value.