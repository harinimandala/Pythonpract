# Fibonacci series

print("-----printing fibonacci series-----")
n = int(input("Please enter a value : "))
a, b = 0, 1
for i in range(0, n):
    c = a + b
    a = b
    b = c
    print(c)

# printing multiplication table for the given number

print("-----printing multiplication table for the given number-----")
n = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

# checking for a prime number

print("-------checking for a prime number------")

n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(f"Given number {n} is not a prime")
        break
else:
    print(f"Given number {n}is a prime number")


# even and odd Number

print("-----even and odd Number-----")
for i in range(2, 11):
    if i % 2 == 0:
        print(f"The given number '{i}' is Even number")
    else:
        print(f"The given number '{i}' is odd number")


# write a program to print 1-100 numbers without numbers which are divisible by  3 or 5

print("-----Printing 1-100 numbers without numbers which are divisible by  3 or 5 ------")

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# write a program to print * in 5x5

print("-----a program to print * in 5x5-----")

for j in range(4):
    for i in range(4):
        print("*", end=" ")
    print()


# write a program to print * in 1-4
print("-----a program to print * in 1- 4----")


for j in range(4):
    for i in range(j+1):
        print("*", end=" ")
    print()

# write a program to print * in 4-1
print("-----a program to print * in 4- 1-----")


for j in range(4):
    for i in range(4-j):
        print("*", end=" ")
    print()

