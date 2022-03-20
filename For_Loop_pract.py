# Basic for Loop

print("-----Basic for loop-----")

fruits = ["Apple", "Mango", "Grapes"]
for x in fruits:
    print(x)

#  Looping Through a String
print("-----Looping Through a String-----")

for x in "Banana":
    print(x)

#    The break Statement
print("-----The break Statement-----")

fruits = ["Apple", "Mango", "Banana", "Grapes"]
for x in fruits:
    if x == "Banana":
        break
    print(x)

#   The continue Statement
print("-----The continue Statement-----")

fruits = ["Apple", "Mango", "Banana", "Grapes"]
for x in fruits:
    if x == "Mango":
        continue
    print(x)

# The range() Function
print("-----The range() Function-----")

for x in range(2, 30, 3):
    print(x)
else:
    print("execution completed")

#  Nested Loops
print("-----Nested Loops-----")

Col = ["Red", "yellow", "Small"]
fru = ["Apple", "Banana", "cherry"]
for x in Col:
    for y in fru:
        print(x, y)

#  Write a program to print first 10 natural number.
print("-----A program to print first 10 natural number.-----")

for x in range(1,11):
    print(x)

#  Write a program to print first 10 even number.
print("-----A program to print first 10 even number.-----")

for e in range(2,11, 2):
    print(e)

#  Write a program to print first 10 odd number.
print("-----A program to print first 10 odd number.-----")

for o in range(1, 22, 3):
    print(o)

# Write a program to print first 10 even numbers in reverse order.
print("-----A program to print first 10 reverse order.-----")
"""i = 20
for x in range(2, 22, 2):
    while i >= 1:
        if i % 2 == 0:
            print(i)
        i = i-1"""

for i in range(20, 0, -2):
    print(i, end=',')

# Write a program to print table of a number accepted from user.
print("-----A program to print table of a number accepted from user.-----")

n = int(input("Enter a number: "))
for i in range(1, 10):
    print(n, "*", i, "=", n*i)

# Write a program to find the factorial of a number.
print("-----A program to find the factorial of a number.-----")

f = int(input("enter a number: "))
fac = 1
for i in range(1, f+1):
    fac = fac*i
print("Factorial of given number is :", fac)

# # Write a program to find a number is prime or not
print("-----A program to find a number is prime or not.-----")

p = int(input("Enter a number: "))
for i in range(2, p):
    if p % 2 == 0:
        print("A prime")
        break
else:
    print("not a prime")





