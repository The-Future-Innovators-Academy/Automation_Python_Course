from modules.clearscreen import clear_screen

# Introduction
print("Hello World") # string
print(100) # integer
print(True) # boolean

clear_screen()

# Variables
hello = "Hello World!"
num1 = 100
bool1 = True

print(bool1)
print(hello)
print(num1)

clear_screen()

# Recieving Input
user_input = input("Enter a sentence: ")
print(user_input)

num_input = input("Enter a Number: ")
print(num_input)

clear_screen()

# Type Conversion

num1_input = ""

while type(num1_input) != int:
    try:
        num1_input = int(input("Enter a number: "))
    except:
        continue


print(num1_input)

clear_screen()

# Arithmetic Operators

num1 = 69
num2 = 21

sum1 = num1 + num2
quotient = num1 / num2
product = num1 * num2

cubed = 16 ** 3

print(quotient)
print(product)
print(sum1)
print(cubed)


# Comparision Operators


# Logical Operators


# If Statements


# Converting Weights Exercise

