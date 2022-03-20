#  1. Single Inheritance parent/base class
print("-----creating single inheritance parent/base class-----")


class Person:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def p_name(self):
        print(f"firstname is: {self.f_name}, lastname is:{self.l_name} ")


class Student(Person):
    def __init__(self, f_name, l_name, year):
        super().__init__(f_name, l_name)
        self.graduation_year = year

    def welcome(self):
        print(f"Welcome {self.f_name} {self.l_name} for {self.graduation_year} graduation year")


print("Parent class")


p = Person("Harini", "Mandala")
p.p_name()


print("Child class")


s = Student("Adithi", "Mandala", 2010)
print(s.f_name)
print(s.l_name)
print(s.graduation_year)
s.welcome()

# 2. Creating Multiple inheritance 2 parents/base  1 child class
print("-----creating Multiple inheritance ## 2 parents/base  1 child class-----")


class Father:

    def __init__(self, father_name):
        self.father_name = father_name

    def dad(self):
        print(self.father_name)


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name

    def mom(self):
        print(self.mother_name)


class Child(Father, Mother):

    def parents(self):
        print(f"father name is: {self.father_name}")
        print(f"child name is: {self.mother_name}")


c = Child(Mother)
c.father_name = "Mogili"
c.mother_name = "Shakunthala"
c.parents()

c = Child(Father)
c.father_name = "Mogili"
c.mother_name = "Shakunthala"
c.parents()

# 3. Multi level Inheritance 1 Grandparent, 1 parent ,1 child
print("---------Multi level Inheritance ##1 Grandparent, 1 parent ,1 child -------")


class Grandfather:

    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name


class Father(Grandfather):

    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name
        Grandfather.__init__(self, grandfather_name)


class Grandchild(Father):

    def __init__(self, grand_child, father_name, grandfather_name):
        self.grand_child = grand_child
        Father.__init__(self, father_name, grandfather_name)

    def grandchild_name(self):
        print("Grand child name: ", self.grand_child)
        print("Grand Father name: ", self.grandfather_name)
        print("Father name: ", self.father_name)


m = Grandchild("Lava", "Rama", "Dasharatha")
m.grandchild_name()

# Sum of 2 numbers
print("-----Sum of 2 numbers-----")


class Num1:
    def __init__(self, first_number):
        self.first_number = first_number


class Num2(Num1):
    def __init__(self, second_number, first_number):
        self.second_number = second_number
        Num1.__init__(self, first_number)


class Add(Num2, Num1):
    def __init__(self, third_number, second_number, first_number):
        self.third_number = third_number
        Num2.__init__(self, first_number, second_number)

    def sum(self):
        print(f"Firs number: {self.first_number}")
        print(f"Second number: {self.second_number}")
        print(f"third number : {self.third_number}")


s = Add(50, 20, 99)
s.sum()


# 4. Hierarchical inheritance 1 parent  3 children
print("-----Hierarchical inheritance ## 1 parent  3 children-----")


class Guardian:

    def func(self):
        print("This function is in Guardian class")


class Child1(Guardian):

    def func1(self):
        print("This function is in Child1 Class")


class Child2(Guardian):

    def func2(self):
        print("This function is in child2 Class")


class Child3(Guardian):

    def func3(self):
        print("This function is in child3 class")


c1 = Child1()
c2 = Child2()
c3 = Child3()
print("------Child1 with Guardina function-----")
c1.func()
c1.func1()
print("-----Child2 with Guardina function-----")
c2.func()
c2.func2()
print("-----Child3 with Guardina function-----")
c3.func()
c3.func3()

# Hybrid Inheritance
print("----- Hybrid Inheritance-----")


class Guardian:

    def func(self):
        print("This function is in Guardian class")


class Child1(Guardian):

    def func1(self):
        print("This function is in Child1 Class")


class Child2(Child1, Guardian):

    def func2(self):
        print("This function is in child2 Class")


class Child3(Guardian):

    def func3(self):
        print("This function is in child3 class")


c1 = Child1()
c2 = Child2()
c3 = Child3()
print("------Child1 with Guardina function-----")
c1.func()
c1.func1()

print("-----Child2 with Guardian function-----")
c2.func()
c2.func2()
c2.func1()

print("-----Child3 with Guardian function-----")
c3.func()
c3.func3()
