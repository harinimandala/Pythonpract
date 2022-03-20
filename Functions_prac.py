# defining normal function
def my_function1():
    print("Hello world..!")


# function with single argument
def my_function(fname):
    print(fname + "@gmail.com")


# Number of Arguments
def my_function_no_of_args(fname, lname):
    print(fname + " " + lname)


# Arbitrary Arguments, *args
def my_function_arb_arg(*kids):
    print("the child names are:", kids[0])


# Keyword Arguments
def key_word_arg(child3, child1, child2):
    print("One among hte children is :", child3)


# Passing a List as an Argument
def li_arg_fun(list):
    for x in list:
        print(x)


# Return Values
def ret_fun(x):
    return 5 * x


#  Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def opera(h, r):
    sum = h + r
    sub = h - r
    mul = h * r
    print(f"sum is: {sum}, sub is: {sub}, multiplication is : {mul}")


# Define a function that accepts roll number and returns whether the student is present or absent.
def attendance(rl):
    list_roll = [101, 105, 107, 109, 108]
    if rl in list_roll:
        print("Present")
    else:
        print("Abscent")

# 3: Define a function in python that accepts 3 values and returns the maximum of three numbers.


def max_num(p, q, r):
    if p > q and p > r:
        print(f"value of p:{p} is greater")
    elif q > p and q > r:
        print(f"value of q:{q} is greater")
    else:
        print(f"value of r:{r} is greater")

#   Define a function that accepts a number and returns whether the number is even or odd.


def even_odd(x):
    if x % 2 == 0:
        print(f"given number: {x} is even")
    else:
        print(f"given number: {x} is odd")

# Define a function which counts vowels and consonant in a word.

def vo_co(word):
    con = 0
    vow = 0
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            vow = vow + 1
        else:
            con = con + 1
    print("count of vowels is", vow)
    print("count of consonents is", con)

# Define a function that returns Factorial of a number.

def fact(x):
    fac = 1
    for i in range(1, (x+1)):
        fac = fac * i
    print(f"factorial of {x} is {fac}")

# Define a function that accepts lowercase words and returns uppercase words.


def low_let(word_l):
    z = word_l.upper()
    print(z)

# Define a function that accepts radius and returns the area of a circle.


def rad_ci(x):
    a = 3.14 * (x**2)
    return a

#   ----------------------End of function definitions-------------------------


# calling defined function
print("-----calling defined function-----")
my_function1()

# calling defined function with single argument
print("-----calling defined function with single argument-----")

my_function("hariniarya910")
my_function("pandanus.ms")
my_function("HR")

# Number of Arguments
print("-----calling function with Number of Arguments-----")
my_function_no_of_args("Harini", "Mandala")
my_function_no_of_args("Adithi", "Mandala")

# Arbitrary Arguments, *args
print("-----calling function with Arbitrary Arguments, *args-----")
my_function_arb_arg("Peetamber", "Dhruv", "Adithi")

# Keyword Arguments
print("-----calling Keyword Arguments-----")
key_word_arg(child1="Archana", child2="koushik", child3="Harini")

# Passing a List as an Argument
print("-----Passing a List as an Argument-----")

fruits = ["Apple", "Banana", "Mango", "Grapes"]
li_arg_fun(fruits)

# Return Values
print("-----functions with Return Values -----")

print(ret_fun(3))
print(ret_fun(5))
print(ret_fun(10))

# Define a function that accepts 2 values and return its sum, subtraction and multiplication.
print("-----A program with a function that accepts 2 values and return its sum, subtraction and multiplication.-----")
h = int(input("enter value for h: "))
r = int(input("enter value for r: "))

opera(h, r)

# Define a function that accepts roll number and returns whether the student is present or absent.
print("-----a function that accepts roll number and returns whether the student is present or absent.-----")

rl = int(input("input a roll number: "))

attendance(rl)

#  3: Define a function in python that accepts 3 values and returns the maximum of three numbers.
print("-----A function in python that accepts 3 values and returns the maximum of three numbers.-----")

p = int(input("Enter a value for p: "))
q = int(input("Enter a value for q: "))
r = int(input("Enter a value for r: "))

max_num(p, q, r)

#  Define a function that accepts a number and returns whether the number is even or odd.
print("----- A function that accepts a number and returns whether the number is even or odd.-----")

x = int(input("Enter a number: "))
even_odd(x)

# Define a function which counts vowels and consonant in a word.
print("-----A function which counts vowels and consonant in a word.-----")

word = input("enter a word : ")
vo_co(word)

# Define a function that returns Factorial of a number.
print("-----A function that returns Factorial of a number.-----")

x = int(input("enter a number: "))
fact(x)

# Define a function that accepts lowercase words and returns uppercase words.
print("-----A function that accepts lowercase words and returns uppercase words.-----")

word_l = input("enter a word in lower case: ")
low_let(word_l)

# Define a function that accepts radius and returns the area of a circle.
print("-----A function that accepts radius and returns the area of a circle.-----")

x = int(input("enter a value: "))
rad_ci(x)
print(rad_ci(x))

