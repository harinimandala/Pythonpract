import datetime
# 1.Normal print statement
print("Hello world..!")
print("--------------end of Normal print statement--------------")


# 2.Multiple objects with sep and end parameters:
print("Hello ", " World", sep="**", end="..!!")
print("/n")
print("-------------end Multiple objects with sep and end parameters--------------")

# 3.Using string concatenation
str0 = "Harini"
str1 = " Mandala"
str2 = "is"
str3 = "Learning"
str4 = "Python"
print(str0+str1+str2+str3+str4)
print("--------------end Using string concatenation--------------")

# 4. concatenation of two different data types:

now = datetime.datetime.now()
str_time = "Current time is: "
print(str_time+str(now))
print("--------------end concatenation of two different data types--------------")


# 5.Using fstrings for string concatenation

now = datetime.datetime.now()
print(f"current time is:, {now}")
num = 8
print(f"given number is  {num}")
str_name = "Harini"
print(f"Given name is:  {str_name} ")

print("--------------end Using fstrings for string concatenation--------------")


#  6. using positional arguments

now = datetime.datetime.now()
print('current time', now)

print("--------------end using positional arguments--------------")

# 7. Using file parameter

scr_file = open("python.txt", 'w')
scr_file.write("hey there...")
print("This is sample text to see printing some text into file using print", file=scr_file)
scr_file.close()
print("--------------end Using file parameter--------------")

# 8. Printing New line:

print("Hello")
print(5*"\n")
print("World")
print("--------------end Printing New line--------------")

# using '
print("I don't have a pen")
print('"Yes", they said')
print("isn\'t it")
print("isn't it")

# with raw  string using r infront.

print("c:\some\name")
print(r"c:\some\name")

print('Py' 'thon')

print("Spam"  "eggs")
print(r'"Spam" "eggs"')
