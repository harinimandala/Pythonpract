# list comprehension
import json

print("----- normal list comprehension-----")
num = [z for z in range(1, 11)]
print(num)

# list comprehension using if loop
print("-----list comprehension using if loop-----")

eve_num = [z for z in range(1, 11) if z % 2 == 0]
print(eve_num)

# list comprehension using if-else loop
print("-----list comprehension using if-else loop-----")

odd_num = [z if z % 2 == 0 else z % 3 == 0 for z in range(1, 11)]
print(odd_num)

print("-----json comprehension-----")
x = '{"Name":"Harini", "age": 33, "Occupation":"Manager"}'
z = json.loads(x)

Q = [l for l in (z)]
print(Q)



