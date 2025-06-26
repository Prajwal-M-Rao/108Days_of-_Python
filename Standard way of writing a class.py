# Standard Way of Declaring a Class in Python

# 1. Define a class using the `class` keyword followed by the class name (PascalCase is recommended).
class Student:  
    # 2. Use the `__init__` constructor method to initialize instance variables.
    def __init__(self, name, usn, num, addr):  
        # 3. `self` represents the instance of the class and allows access to attributes.
        # 4. Declare instance variables and assign values received as parameters.
        self.name = name   # Student's name
        self.usn = usn     # Unique university serial number
        self.num = num     # Contact number
        self.addr = addr   # Address

# 5. Create objects (instances) of the class by calling the constructor with required arguments.
s1 = Student("Prajwal", '4SU21AD035', 8317371953, 'Chintamani')
s2 = Student('Raavana', '4SU21AD100', 9945321098, 'Lanka')

# 6. Access instance variables using the object name followed by the attribute.
print(s1.name)  # Output: Prajwal
print(s2.name)  # Output: Raavana
