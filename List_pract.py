# 1.creating list
list_1 = ["Harini", "Mandala", 1, 5.1, "F", "F", "Python", "Programming", "Mandala"]
print(list_1)
print("--------End of creating & printing list----------")

# accessing the list
el = list_1[2]
print(f"value of the given index number is {el}")
el_n = list_1[-4]
print(f"value of given negative index is {el_n}")

print("--------End of accessing the elements of +ve and -ve index & printing list----------")

# slicing in list
print(list_1)
el_sl = list_1[1:6]
print(f"sliced list is : {el_sl}")

el_sl = list_1[-6:-2]
print(f"negative index slicing of the list is : {el_sl}")

print("--------End of slicing in list of +ve and -ve index & printing list----------")

# adding to list

list_1.append("language")
print(list_1)
# append accepts only 1 element and adds at the ned of the list

list_1.extend(["code", "Yes", "NO"])
print(list_1)

list_1.insert(-1, 101)
print(list_1)
print("--------End of adding to list of +ve and -ve index & printing list----------")

# remove elements in list

list_1.remove(101)
print(list_1)
#  removes element no need to mention element
print("------------------")
list_1.pop()
print(list_1)
# removes the last element
list_2 = ["Harini", 1, 0, 9, 'S']
print(list_2)
list_2.clear()
print(list_2)
print("--------End of remove elements in list & printing list----------")

# returns given string repetitions
print(list_1.index("Python"))

print(list_1.count("Mandala"))

print("--------End of returns given string repetitions in list & printing list----------")


# sort orders of list

list_3 = [12, 9, 22, 4, 99]
print(list_3)

#  ascending order
print("sorting a list in ascending order")
list_3.sort()
print(list_3)

#  descending order
print("sorting a list in descending order")
list_3.sort(reverse=True)
print(list_3)

print("--------End of sort orders of list using numbers & printing list----------")

# # sort orders of string list

fruits = ["mangoes", "kiwi", "guava", "apple", "sapota", "banana"]
print(fruits)

# ascending order
fruits.sort()
print(fruits)

# descending order
fruits.sort(reverse=True)
print(fruits)

print("--------End of sort orders of  string list using numbers & printing list----------")

# Nested Lists....

list_ns = [16, 12, 89, 90, [34, "Harini", "Pyhton"], 23, 56, 98]
print(list_ns[4])
print(list_ns[4][1])
print("--------End of Nested Lists & printing list----------")


# List Comprehension...

squares = [i**2 for i in range(1, 11)]
print(squares)

#   printing 2 table using list comprehension

two_table = [i for i in range(2, 21, 2)]
print(two_table)
print("printing 2 table")
print("--------End of 2 table using List Comprehension  & printing list----------")


fourteen_table = [i for i in range(14, 140, 14)]
print(fourteen_table)
print("printing 14 table")

fruits = ["apples", "mango", "pineapple", "strawberry", "banana", "beer"]
new_fruits_list = [f for f in fruits if 'm' in f]
print(new_fruits_list)

print("--------End of List Comprehension & printing list----------")

# Looping in List

list_tw = [2, 4, 6, 8, 10]
for i in list_tw:
    print(i)
print("----End of for loop----------")
i = 0
while i <= 10:
    print(i)
    i = i+1
print("----End of while loop----------")

odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
pair = [(x, y) for x in odd for y in even if x != y]
print(pair)

print("----End of list comprehension using list----------")


# COPY OF LIST
li = [1, "SHE", 2, "is", 3, "Capable"]
print(li)
lc = list(li)
print(lc)
lc.insert(2, 16)
print(lc)
li.append(4)
print(li)
print(lc)
li.extend(["yes", 6, "Capable"])
print(li)
print(lc)
print("----End of COPY OF LIST using list----------")


#  Join list

li_1 = [1, 2, 3]
li_2 = [4, 5, 6]
li_3 = li_1+li_2
print(li_3)
print("----End of Join list using + ----------")

li_a = ['a', 'b', 'c']
li_b = [1, 2, 3]

for x in li_b:
    li_a.append(x)
print(li_a)
print("----End of Join list append ()----------")

li_a.extend(li_b)
print(li_a)
print("----End of Join list using extend ()----------")

# Nested list
print("-----Nested List-----")
a = [2, 4, 6, 8]
x = ['a', 'e', 'i', 'o', 'u']
y = [a, x]

print(y)
print(y[0][2])
print(y[1][-1])

name = ["Harini", "Adithi"]
print(name)
n1 = name[0]
print(n1)
n1 = name[0][:4]
print(n1)


l = [12, 14, 90, 1, 10]
print(l)
l.sort()
print(l)
l.reverse()
print(l)