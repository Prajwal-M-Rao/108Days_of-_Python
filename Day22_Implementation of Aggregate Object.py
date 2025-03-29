# Charger class (can exist independently)
class Charger:
    def __init__(self, brand):
        self.brand = brand

    def charge(self):
        print(f"{self.brand} charger is charging the device")


# Mobile class (aggregates a Charger object)
class Mobile:
    def __init__(self, name, charger):
        self.name = name
        self.charger = charger  # Aggregation: Mobile holds a reference to Charger

    def start_charging(self):
        if self.charger:
            self.charger.charge()
        else:
            print("No charger connected")


# Creating a Charger object
c = Charger("Samsung")

# Creating a Mobile object and passing the existing Charger object
m = Mobile("Galaxy S24", c)

# Using the Mobile object to start charging
m.start_charging()

# The Charger object still exists even if the Mobile object is deleted
del m
c.charge()  # The charger is still usable
