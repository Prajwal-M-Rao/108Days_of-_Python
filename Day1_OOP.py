#If an object is created, Python VM will perform basicaaly 3steps
# 1. Creates a seperate block of memory with address
# 2. Searches for a method called "__init__" and allocates memory in to the varialbles in the block
# 3. Exectues

# The below mentioned code snippet is a simple example for a class#



class Fan:
    def __init__(self):
        self.brand="Usha"
        self.color="Brown"
        self.cost=3000
        self.no_of_blades=4
    def rotate_speed(self):
        print("Fan is rotating at the 3 speed")
    def revolution(self):
        print("Fan cant revolve")
f=Fan()
print(f.brand)
print(f.cost)
print(f.no_of_blades)
print(f.color)
print("\n")

# To change the values for the variables alredy created
f.cost=5000
f.color="Peach"
print(f.color)
print(f.cost)

# To create new Variables
f.type="Table Fan"
print(f.type)
