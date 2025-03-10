#a string is a sequence of characters enclosed in either single quotes ('), double quotes ("), or triple quotes (''' """)

#Properties
    #Immutable – Strings cannot be changed after creation.
    #Indexing – Each character in a string has an index starting from 0.
    #Slicing – A substring can be extracted using slicing.

str="RajaRamMohanRoy"
print(str)
print(len(str))

#Indexing
print(str[0])
print(str[12])
print(str[-1])
print(str[-12])
print(str[-10])

#Slicing
print(str[0:4])
print(str[10:14])
print(str[:6])
print(str[12:])
print(str[:])
print(str[::2])
print(str[::-1])

print(str[12:3])
print(str[-11:-3])
print(str[:-5:-1])
print(str[-12:-2])
print(str[-8:-14])
print(str[5::-1])

print(str[8:11:0])