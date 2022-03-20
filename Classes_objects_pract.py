import math
# 1.simple class creation
print("-----simple class creation-----")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_data(self):
        print(f"Hello my name is:{p1.name}")


p1 = Person("Harini", 33)
print(p1.name)
print(p1.age)
p1.age = 2
print(p1.age)
p1.person_data()

# 2. A program to add 2 numbers using class/object methods:
print("----- A program to add 2 numbers using class/object methods:-----")


class Operations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(a, b):
        s = a + b
        return s


s1 = Operations

print(s1.sum(12, 90))


# 3.A program to find the number even/odd using class/object methods:
print("-----A program to find the number even/odd using class/object methods-----")


class Finder:

    def __init__(self, n):
        self.n = n

    def even(self):

        if self.n % 2 == 0:
            print(f"given number is {self.n} and its even")
        else:
            print(f"given number is {self.n} and its odd")


num = Finder(int(input("enter a number: ")))
num.even()

# 4. A program to find the prime of a given number:
print("-----A program to find the factorial of a given number-----")


class Prime:
    def __init__(self, z):
        self.z = z

    def pr_num(self):

        if self.z % 2 == 0:
            print(f"Given number {self.z} is not a prime number")
        else:
            print(f"Given number {self.z} is a prime number")


pr = Prime(7)
pr.pr_num()

# class with instance variables and class/static variable
print("-----class with instance variables and class/static variable -----")


class Student:
    school = "Scholars'"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg_marks(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is an instance of static method..")


s1 = Student(55, 98, 87)
s2 = Student(87, 93, 88)

x = (s2.avg_marks())
y = (math.ceil(x))

print(Student.school_name())
print(f"Student1 has the average of {s1.avg_marks()}")
print(f"Student2 has an average of {y}")
print(Student.info())
