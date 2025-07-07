# Function to check if a number is a Happy Number
def Happy_Number(num):
    # If number becomes 1, it's a Happy Number
    if num == 1:
        return True
    # If number becomes 4, it will enter a cycle (not happy)
    elif num == 4:
        return False

    sum = 0
    # Calculate the sum of the squares of each digit
    while num > 0:
        digit = num % 10          # Extract last digit
        sum += digit ** 2         # Square it and add to sum
        num = num // 10           # Remove last digit

    # Recursively check the new sum
    return Happy_Number(sum)

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is happy
flag = Happy_Number(num)

# Display the result
if flag:
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")
