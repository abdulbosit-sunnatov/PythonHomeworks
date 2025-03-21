# Task 1
username = input("Enter username: ")
password = input("Enter password: ")
print("Valid" if username and password else "Invalid")

# Task 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Equal" if a == b else "Not equal")

# Task 3
num = int(input("Enter a number: "))
print("Positive and even" if num > 0 and num % 2 == 0 else "Not positive or not even")

# Task 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("All different" if len(set([a, b, c])) == 3 else "Not all different")

# Task 5
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Same length" if len(str1) == len(str2) else "Different length")

# Task 6
num = int(input("Enter a number: "))
print("Divisible by 3 and 5" if num % 3 == 0 and num % 5 == 0 else "Not divisible by both")

# Task 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater than 50" if (a + b) > 50 else "Not greater than 50")

# Task 8
num = int(input("Enter a number: "))
print("Between 10 and 20" if 10 <= num <= 20 else "Not in range")


