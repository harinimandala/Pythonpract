# String Methods
print("----Normal string -----")
str1 = "hello world!"
print(str1)

print("-----capitalize string----- with capitalize()------")
s = str.capitalize(str1)
print(s)

# str.center(width[, fillchar])¶
print("----String slicing-------")

s2 = str1[1:5]
print(s2)

# String will not allow assignment
"""str1[0] = "G"
print(str1)"""

# String manipulations.....
print("-------String manupulations to replace a word using replace ()---------")
Greetings = ("Hello World")
G1 = Greetings.replace("Hello", "Hi")
print(Greetings)
print(G1)

print("-------String manupulations to split a sentence using split ()---------")


Greetings = "Hello_ World_How_ are_you"
G1 = Greetings.split('_')
print(Greetings)
print(G1)

print("-----String manupulations to join a sentence using join ()-------")
name = ("Harini", "Mandala")
full_name = " ".join(name)
print(name)
print(full_name)
