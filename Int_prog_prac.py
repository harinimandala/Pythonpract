# 1.Write a program to find a number is prime or not
print("-----A program to find a number is prime or not.-----")

p = int(input("Enter a number: "))
for i in range(2, p):
    if p % 2 == 0:
        print("A prime")
        break
else:
    print("not a prime")

# 2.Write a program to print table of a number accepted from user.
print("-----A program to print table of a number accepted from user.-----")

n = int(input("Enter a number: "))
for i in range(1, 10):
    print(n, "*", i, "=", n*i)

# 3.Write a program to find the factorial of a number.
print("-----A program to find the factorial of a number.-----")

f = int(input("enter a number: "))
fac = 1
for i in range(1, f+1):
    fac = fac*i
print("Factorial of given number is :", fac)

