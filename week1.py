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

clear_screen()

# Comparision Operators
num1 = 5
num2 = 5

less_than = num1 < num2
print(less_than)

greater_than = num1 > num2
print(greater_than)

equal_to = num1 == num2
print(equal_to)

clear_screen()


# Logical Operators
num1 = 1
num2 = 21
num3 = 69

compare1 = num1 < num2 and num2 < num3
print(compare1)

clear_screen()
# If Statements
num1 = 87
num2 = 420

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

# Converting Weights Exercise
# in to ft, ft to miles, m to km, cm to m, g to kg
    
while True:
    user_input = input("What do you want to convert (q to quit): ")
    if user_input == "q":
        break
    

    if user_input == "in":
        inches = int(input("How many inches do you want to convert to feet: "))
        print(inches / 12)
    elif user_input == "ft":
        feet = int(input("How many feet do you want to convert to miles: "))
        print(feet / 5280)
    elif user_input == "m":
        meters = int(input("How many meters do you want to convert to km: "))
        print(meters / 1000)
    else:
        print("Incorrect Input")


