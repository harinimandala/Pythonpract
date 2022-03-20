# SET IN PYTHON

set1 = {"Adithi", "F", 1, 12.89, "F"}
print(set1)
print("--------End of set creation-------")

le_se = (len(set1))
print(le_se)
print("--------End of length of set by len ()-------")

for i in set1:
    print(i)

print("Adithi" in set1) # returns True/False based on availability
print("--------End of accessing elements in set -------")


set2 = {1, 2, 3, 4}
set1.update(set2)
print(set1)

print(set2)
li_se = [101, "Yes", "N"]
set2.update(li_se)
print(set2)

set1.add("Dhruv")
print(set1)

set1.add("Peetamber")
print(set1)
print("--------End of add element by add ()-------")

set1.remove(1)
print(set1)

set1.discard("Harini") # removes the element if it exists but will not return any error if there is no element.
print(set1)

set1.pop()
print(set1)

set3 = {1, 90, 22}
print(set3)
set3.clear()
print(set3)
set4 = {'A', 'B', 'C'}
print(set4)
del set4

print("--------End of set remove element by remove ()-------")

oldset = {2, 4, 6, 8}
newset = {s**2 for s in oldset}
print(newset)
cubes = {c**3 for c in {1, 2, 3, 4, 5, 6}}
print(cubes)

print("--------End of set remove element by remove ()-------")

# Join Two Sets::

set_c1 = {1, 2, 3}
set_c2 ={"a", "b", "c", "d"}
set_c3 = set_c1.union(set_c2)
print(set_c3)

set1= {"I", "U"}
set2 = {1, 2, 3}
set4 = set1.union(set2)
print(set4)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
s = x.intersection(y)
print(s)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)
print("--------end of Join Two Sets---------")

s = {1, 2, 3, 4}
s1 = s.copy()
print(s1)
print("----End of copy-----")
sd = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 7, 8, 9}
sa = sd.difference(s2)
print(sa)

sa1 = s2.difference(sd)
print(sa1)

sd = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 7, 8, 9}
sd.difference_update(s2)
print(sd)
print("----End of difference-----")

sd.intersection(s2)
print(f"difference is {sd} ")

sd.intersection_update(s2)
print(sd)

sdi = sd.isdisjoint(s2)
print(sdi)

sdi = sd.issubset(s2)
print(sdi)

ssups = sd.issuperset(s2)
print(ssups)

