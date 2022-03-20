# TUPLES
print("-------Tuple with same data type------------")
tuple1 = (1, 2, 3, 4, 5)
print(f"{tuple1}")

print("-------Tuple with different data type------------")
tuple2 = (16, "Harini", 5.1, 'F')

# check if item exists..
if "Harini" in tuple2:
    print("Yes, Harini exists in the list")
print("-------check if item exists in Tuple------------")

print(tuple2)

print("-------Accessing Tuple with +ve and -ve index------------")
print(tuple2[1])
print(tuple1[-5])
print(tuple1[:4])
print(tuple2[-4:-1])
print(tuple1[-1::])
print(len(tuple1))  # gives length of the tuple

print("-------Change Tuple by creating a list and list back to tuple------------")
tup = ("Python", "Language", "JS", " ")
print(tup)

tup_con_ls = list(tup)
tup_con_ls.append("Language")
print(len(tup))

tup_con_ls[4] = "Springboot"
tup = tuple(tup_con_ls)
print(tup)

print("-----------------")
tup = ("Python", "Language", "JS", " ")
tup1 = ("Java",)
tup += tup1
print(tup)

print("------Loops in tuple using for-----------")

# Loops in tuple can be done in 3 ways for ,range, while
tup = ("Python", "Language", "JS", " ",)
for x in tup:
    print(x)
print("------Loops in tuple using range-----------")

tup_l = ("Python", "Language", "JS", " ",)
for i in range(len(tup_l)):
    print(tup_l[i])

print("------Loops in tuple using while-----------")

tup_wl = (2, 4, 6, 8, 10)
i = 0
while i < len(tup_wl):
    print(tup_wl[i])
    i = i + 1


print("------Joining Tuple with + operator -----------")


tup_1 = (1, 2, 3, 4)
tup_2 = (101, 102, 103, 104)
tup_3 = tup_1 + tup_2
print(tup_3)

print("------Multiply Tuple with * operator -----------")

tup_1 = (1, 2, 3, 4)*3
print(tup_1)

s = tup_1.index(4)
print(s)
s = tup_1.count(2)
print(s)
