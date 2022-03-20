# iter() method which is used to get an iterator
print("-----iter() method which is used to get an iterator-----")


mytuple = ("Harini", "Adithi", "Dhruv", "Peetamber")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 2. containing a sequence of characters:
print("-----containing a sequence of characters:-----")

mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 3.Looping Through an Iterator.
print("-----Looping Through an Iterator-----")

mytuple_fruits = ("Microsoft", "Google", "TCS", "Facebook")
for x in mytuple_fruits:
    print(x)

print("-----Looping string through an Iterator-----")

my_fruit = "JACKFRUIT"
for x in my_fruit:
    print(x)

# __iter__ and __next__
print("-----Create an Iterator---- using __iter__/__next__")

class Count:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        n = self.a
        self.a += 1
        return n

c = Count()
myiter1 = iter(c)

print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

# printing 20 digits using  iter/ next
print("-----printing 20 digits using  iter/ next-----")


class Number:
    def __iter__(self):
        self.z = 1
        return self

    def __next__(self):
        if self.z <= 10:
            u = self.z
            self.z += 1
            return u
        else:
            raise StopIteration


mynumb = Number()
i = iter(mynumb)

for x in i:
    print(x)


