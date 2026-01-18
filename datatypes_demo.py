# datatypes_demo.py
# Task 2: Variables, Data Types & Type Conversion
# Step 1: Declare variables of different data type
age = 18                 # Integer
height = 176.5           # Float
name = "Dhiraj"          # String
is_student = True        # Boolean

# Step 2: Print types of variables

print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))

print("\n-------------------------------\n")

# Step 3: Arithmetic operations

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)

print("\n-------------------------------\n")

# Step 4: Type conversion (string to int & float)

num1 = input("Enter an integer number: ")
num2 = input("Enter a float number: ")

# Converting string input to int and float
num1 = int(num1)
num2 = float(num2)

print("Sum:", num1 + num2)

print("\n-------------------------------\n")

# Step 5: Handle invalid input using try-except

try:
    value = int(input("Enter a valid integer: "))
    print("You entered:", value)
except ValueError:
    print("Invalid input! Please enter numbers only.")

print("\n-------------------------------\n")

# Step 6: String and number concatenation

print("Name:", name)
print("Age is", age)             # Using comma
print("Age is " + str(age))      # Using type conversion

print("\n-------------------------------\n")

# Step 7: Demonstrate dynamic typing

x = 10
print(x, type(x))

x = "Hello Python"
print(x, type(x))

x = 3.14
print(x, type(x))

