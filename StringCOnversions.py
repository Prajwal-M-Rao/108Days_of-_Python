# Prompting the user to enter a string
print("Enter the input String: ")
str = input()

i = 0  # Initializing index for iteration
newstr = ''  # Empty string to store converted characters

# Converting uppercase letters to lowercase
while i <= len(str) - 1:
    data = str[i]
    ascii = ord(data)  # Getting ASCII value of character
    if 65 <= ascii <= 90:  # Checking if character is uppercase (A-Z)
        newascii = ascii + 32  # Converting to lowercase by adding 32
        convchar = chr(newascii)  # Converting ASCII to character
        newstr += convchar  # Appending to new string
    else:
        newstr += data  # Keeping other characters unchanged
    i += 1  # Moving to the next character
print(newstr)  # Printing the converted lowercase string

# Resetting index for the next conversion
i = 0
newstr = ''  # Resetting new string for uppercase conversion

# Converting lowercase letters to uppercase
while i <= len(str) - 1:
    data = str[i]
    ascii = ord(data)  # Getting ASCII value of character
    if 97 <= ascii <= 122:  # Checking if character is lowercase (a-z)
        newascii = ascii - 32  # Converting to uppercase by subtracting 32
        convchr = chr(newascii)  # Converting ASCII to character
        newstr += convchr  # Appending to new string
    else:
        newstr += data  # Keeping other characters unchanged
    i += 1  # Moving to the next character
print(newstr)  # Printing the converted uppercase string

# Resetting index for the next conversion
i = 0
newstr = ''  # Resetting new string for swap case conversion

# Swapping case: Converting uppercase to lowercase and vice versa
while i <= len(str) - 1:
    data = str[i]
    ascii = ord(data)  # Getting ASCII value of character
    if 65 <= ascii <= 90:  # If character is uppercase
        newascii = ascii + 32  # Convert to lowercase
        convchar = chr(newascii)
        newstr += convchar
    elif 97 <= ascii <= 122:  # If character is lowercase
        newascii = ascii - 32  # Convert to uppercase
        convchr = chr(newascii)
        newstr += convchr
    else:
        newstr += data  # Keeping other characters unchanged
    i += 1  # Moving to the next character
print(newstr)  # Printing the swapped case string

# Using built-in string methods for case conversion
print(str.upper())  # Converts the entire string to uppercase
print(str.lower())  # Converts the entire string to lowercase
print(str.swapcase())  # Swaps the case of each character in the string
