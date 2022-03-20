import re

# RegEx in Python with search key word
print("-----RegEx in Python with search key word-----")

txt = "The rain in Spain"
x = re.search("in.*rain$", txt)
if x:
    print("Given String matches")
else:
    print("Given string doesnot match")

# The findall() Function
print("------The findall() Function-----")

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

print("returns empty list whn=en the txt doesnt match")

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# The search() Function
print("-----The search() Function-----")

txt = "The rain in Spain"
x = re.search("pa", txt)
print(x.start())

# The split() Function
print("-----The split() Function-----")
txt = "The rain in Spain"
x = re.split("in", txt, 1)
print(x)

# The sub() Function
print("-----The sub() Function-----")

txt = "The rain in Spain"
x = re.sub("ra", "ga", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
