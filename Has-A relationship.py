#The Has-A relationship (also known as Composition) is a fundamental OOP concept where one class contains an instance of another class as an attribute.
# Instead of inheriting from a class (as in the Is-A relationship), a class "has" another class within it.

# Radio class (Used inside Car class)
class Radio:
    def turnon(self, x):
        if x == 1:
            print("Radio is on")
        else:
            print("Radio is off")

# Car class (Has-A relationship with Radio)
class Car:
    def __init__(self, min, max):
        self.cmin = min  # Minimum speed
        self.cmax = max  # Maximum speed
        self.r = Radio()  # Car has a Radio object

c1 = Car(50, 120)
print(c1.cmin)  # Output: 50
print(c1.cmax)  # Output: 120

c1.r.turnon(1)  # Output: Radio is on
c1.r.turnon(2)  # Output: Radio is off
