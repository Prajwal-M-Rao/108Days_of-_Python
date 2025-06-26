#Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit (a class)
class Student:
    def __init__(self):
        self.__name = ''

    def getter(self):
        return self.__name

    def setter(self, value):
        self.__name = value

s1 = Student()
s1.setter("PMRao")
res = s1.getter()
print(res)

# Encapsulation using Property Function
class Student:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):  # Getter method
        return self.__name

    @name.setter
    def name(self, value):  # Setter method
        self.__name = value

s1 = Student()
s1.name = "PMRao"  # ✅ No need to call setter explicitly
print(s1.name)  # ✅ No need to call getter explicitly


# Property Decorator
class Student:
    def __init__(self):
        self.__name=''

    @property
    def getset(self):
        return self.__name

    @getset.setter
    def getset(self,value):
        self.__name=value

s1=Student()
s1.getset="PMRao"
res=s1.getset
print(res)
