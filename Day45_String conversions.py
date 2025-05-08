arr=input("Enter a string: ")

def low_to_upp(arr):
    newstr = ""
    for i in arr:
        if "a"<=i<="z":
            newstr+=chr(ord(i)-32)
        else:
            newstr+=i
    return newstr

def Upper_to_lower(arr):
    newstr = ""
    for i in arr:
        if "A"<=i<"Z" :
            newstr+=chr(ord(i)+32)
        else:
            newstr+=i
    return newstr

def swap_case(arr):
    newstr=""
    for i in arr:
        if "A"<=i<"Z" :
            newstr+=chr(ord(i)+32)
        elif "a"<=i<="z":
            newstr+=chr(ord(i)-32)
        else:
            newstr+=i
    return newstr

print("Original Array: ",arr)
print("Lower to upper Array: ",low_to_upp(arr))
print("Upper to lower Array: ",Upper_to_lower(arr))
print("Swap case array: ",swap_case(arr))