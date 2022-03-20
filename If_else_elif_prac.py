# If statements:
print("----Simple If statement-------")
a = 1000
b = 10000
if a > b:
    print("a is greater that b")
else:
    print("b is greater than a")

print("-----if elif statement---------")

a = 55
b = 550
if a > b:
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater than a")

print("-----and or conditions---------")
print("--------and----------")

x = 10
y = 20
z = 30

if x > y and x > y:
    print("x is greater")
elif y > x and y > z:
    print("y is greater")
else:
    print("z is greater")

print("--------or----------")
x = 10
y = 20
z = 30

if x > y or x > z:
    print("any one statement is true")
else:
    print("x is smaller")

print("--------Nested If----------")

x = 10
if x > 10:
    print("x is above 10")
    if x > 20:
        print("x is above 20")
    else:
        print("x is between 10-20")
else:
    print("pass")
# 1. Write a program to check whether a person is eligible for voting or not. (accept age from user)

print("---- a program to check whether a person is eligible for voting or not. (accept age from user)----")

age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#  2.Write a program to check whether a number entered by user is even or odd
print("-- A program to check whether a number entered by user is even or odd---")

chc_num = int(input("enter a number to check even or odd: "))
if chc_num % 2 == 0:
    print("given number is even")
else:
    print("given number is odd")
# 3. Write a program to check whether a number is divisible by 7 or not.

print("---- A program to check whether a number is divisible by 7 or not.----")

num = int(input("enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("not divisible by 7")

# 4. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".

print("---Write a program to display 'Hello' if a number entered by user is a multiple of five otherwise 'Bye'.---")

num1 = int(input("enter a value: "))
if num1 % 5 == 0:
    print("Hello World..!")
else:
    print("Bye")

#  5. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#     Unit                                                     Price
# First 100 units                                             no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
print("---a program to calculate the Electricity bill printing based on som criteria------")
bill = 0
no_units = int(input("Enter number of units: "))
if no_units <= 100:
    print("No charges to be paid")
elif no_units > 100 and no_units <= 200:
    bill = (no_units - 100) * 5
    print("your bill is", bill)
elif no_units > 200:
    bill = (no_units - 200) * 10
    print(f"your bill is", bill)

#  6.Write a program to display the last digit of a number
print("-----a program to display the last digit of a number-----")


