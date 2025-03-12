# ------------------------- String Manipulation in Python -------------------------

# Defining a string with leading and trailing spaces
string = "   Raavana Rao     "
print("Original String with spaces:", repr(string))  # Using repr() to show spaces clearly

# Removing leading spaces
string_lstrip = string.lstrip()
print("After removing leading spaces:", repr(string_lstrip))

# Removing trailing spaces
string_rstrip = string.rstrip()
print("After removing trailing spaces:", repr(string_rstrip))

# Removing both leading and trailing spaces
string_strip = string.strip()
print("After removing both leading and trailing spaces:", repr(string_strip))

# ------------------------- Removing spaces from user input -------------------------

# Taking a string input from the user
user_input = input("\nEnter a string (spaces will be removed): ")
print("Original Input:", repr(user_input))

# Removing spaces using a loop
new_string = ''
for char in user_input:
    if char != " ":
        new_string += char
print("String without spaces:", repr(new_string))

# Alternative, more efficient approach using replace()
print("Alternative method (using replace()):", repr(user_input.replace(" ", "")))

# ------------------------- String Operations -------------------------

# Taking user input for string operations
user_string = input("\nEnter a string for various string operations: ")
print("You entered:", user_string)

# Finding the length of the string
print("Length of the string:", len(user_string))

# Counting occurrences of the word 'you' in the string
print("Occurrences of 'you':", user_string.count("you"))

# Checking if 'you' is present in the string
search_word = 'you'
if search_word in user_string:
    print(f"'{search_word}' found at index:", user_string.find(search_word))
    print(f"Last occurrence of '{search_word}' at index:", user_string.rfind(search_word))
else:
    print(f"'{search_word}' not found in the given string.")

# Finding a substring safely
search_substring = "Rohit"
index = user_string.find(search_substring)
if index != -1:
    print(f"'{search_substring}' found at index:", index)
else:
    print(f"'{search_substring}' not found in the string.")

# ------------------------- Checking String Properties -------------------------

# Taking user input to check character composition
check_string = input("\nEnter a string to check its composition: ")

# Checking what type of characters are present
if check_string.isalpha():
    print("The string contains only alphabets.")

elif check_string.isdigit():
    print("The string contains only numbers.")

elif check_string.isalnum():
    print("The string contains both alphabets and numbers.")

else:
    print("The string contains special characters.")

# ------------------------- String Formatting -------------------------

print("\nEnter your details:")
name = input("Enter your Name: ")
age = input("Enter your Age: ")
blood_group = input("Enter your Blood Group: ")

# Displaying user details using format()
print("\nUser Details (Using .format() method):")
print("Name: {}".format(name))
print("Age: {}".format(age))
print("Blood Group: {}".format(blood_group))

# Alternative method using f-strings (Recommended)
print("\nUser Details (Using f-strings):")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Blood Group: {blood_group}")

# ------------------------- End of Program -------------------------
