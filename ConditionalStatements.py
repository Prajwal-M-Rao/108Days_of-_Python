#Conditional Statements - used to check for any conditions
# there are 3 types of conditional statements in Python

a=int(input("Enter a value : "))
b=int(input("Enter another value : "))
if(a>b):
    print("A is greater\n")
elif(b>a):
    print("B is greater\n")
else: print("Both are equal\n")


#Loops- used to reduce the code length if any repeated work has to be done
#We use 2 types of loop in Python, For and While loop
for i in 1,2,3,4,5:
    print(i)
print("\n")
for i in range(3):
    print(i)
print("\n")
for i in range(3,10):
    print(i)
print("\n")
for i in range(3,10,2):
    print(i)
