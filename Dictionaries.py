# ---------------------- DICTIONARIES ----------------------
student = {
    'name': "Rao",
    'age': 25,
    'add': 'Bangalore'
}
print(student)
print("Keys:", student.keys())
print("Values:", student.values())

# Creating a dictionary for employee information
emp_info = {
    'name': 'Rama',
    'empid': 101,
    'editing': 'SE',
    'mob': 954862,
    'addr': 'Mysore'
}

# Display the full dictionary
print("Employee Info:", emp_info)

# Accessing specific values using keys
print("Employee Name:", emp_info['name'])
print("Employee Designation (editing):", emp_info['editing'])

# ---------------------- TRAVERSING THE DICTIONARY ----------------------

# Printing only the keys
print("\nKeys in the dictionary:")
for key in emp_info:
    print(key)

# Printing values using keys
print("\nValues using keys:")
for key in emp_info:
    print(emp_info[key])

# Printing only the values using .values()
print("\nValues directly:")
for value in emp_info.values():
    print(value)

# Printing key-value pairs using .items()
print("\nKey-Value pairs:")
for item in emp_info.items():
    print(item)  # item is a tuple (key, value)
