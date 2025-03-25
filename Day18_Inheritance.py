'''
class CargoPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")
    def carryC(self):
        print("The plane carries Cargo\n")

class PassengerPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")
    def carryP(self):
        print("The plane carries Passengers\n")

class FighterJetPlane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")
    def carryF(self):
        print("The plane carries Fighter Jets\n")

# Creating instances
c = CargoPlane()
p = PassengerPlane()
f = FighterJetPlane()

# Calling methods
c.takeoff()
c.fly()
c.land()
c.carryC()

p.takeoff()
p.fly()
p.land()
p.carryP()

f.takeoff()
f.fly()
f.land()
f.carryF()
'''

#Now lets see the same code with the concept of Inheritance

#Inheritance allows one class (child) to derive attributes and methods from another class (parent). It promotes code reuse and establishes a relationship between classes.
# Base class with common functionality
class Plane:
    def takeoff(self):
        print("The plane is in takeoff")
    def fly(self):
        print("The plane is flying")
    def land(self):
        print("The plane is landing")

# Subclasses inheriting from Plane
class Cargo(Plane):
    def carry(self):
        print("The plane carries Cargo\n")

class Passenger(Plane):
    def carry(self):
        print("The plane carries Passengers\n")

class FighterJet(Plane):
    def carry(self):
        print("The plane carries Fighter Jets\n")

# Creating instances
c = Cargo()
p = Passenger()
f = FighterJet()

# Calling methods
c.takeoff()
c.fly()
c.land()
c.carry()

p.takeoff()
p.fly()
p.land()
p.carry()

f.takeoff()
f.fly()
f.land()
f.carry()
