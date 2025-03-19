# Task 1
num = float(input("Enter a float number: "))
print(round(num, 2))

# Task 2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))

# Task 3
km = float(input("Enter kilometers: "))
meters = km * 1000
centimeters = km * 100000
print("Meters:", meters)
print("Centimeters:", centimeters)

# Task 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Integer division:", a // b)
print("Remainder:", a % b)

# Task 5
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Task 6
num = int(input("Enter a number: "))
print("Last digit:", num % 10)

# Task 7
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")



