class A:
    def __init__(self):
        self.a = 10  

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's constructor
        self.b = 20  

class C(B):
    def __init__(self):
        super().__init__()  # Calls B's constructor
        self.c = 30  

cf = C()  

print(cf.c)  # Output: 30
print(cf.b)  # Output: 20
print(cf.a)  # Output: 10
