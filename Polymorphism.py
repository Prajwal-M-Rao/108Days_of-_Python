class Plane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")

class CargoPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing\n")

class PassengerPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing\n")

class FighterJetPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")

c=CargoPlane()
p=PassengerPlane()
f=FighterJetPlane()

def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()

#Polymorphism (1:many)

allowPlane(c)
allowPlane(p)
allowPlane(f)

'''
The same code can be written with integration of Inheritance and Polymorphism

class Plane:
    def takeoff(self):
        print("The plane is in takeoff")
    
    def fly(self):
        print("The plane is flying")
    
    def land(self):
        print("The plane is landing\n")

class CargoPlane(Plane):
    pass

class PassengerPlane(Plane):
    pass

class FighterJetPlane(Plane):
    pass

# Creating instances
c = CargoPlane()
p = PassengerPlane()
f = FighterJetPlane()

# Function demonstrating polymorphism
def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()

# Calling function with different objects
allowPlane(c)
allowPlane(p)
allowPlane(f)

'''
