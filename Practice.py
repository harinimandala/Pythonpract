"""import mymodule
import math"""
"""mymodule.greetings("Harini")

a = mymodule.person1["age"]
print(a)"""


def search(lst, n):

    for i in lst:
        if i == n:
            return True
    else:
        return False


lst = [13, 78, 56, 5, 45]
n = 45

if search(lst, n):
    print("Found")
else:
    print("Not found")

