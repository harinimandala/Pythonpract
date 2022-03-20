# defining normal Lambda function
from functools import reduce
reduce(lambda a, b: a*b, [4, 3, 2, 1])

j = lambda a, b: (a+b)**2
j(4, 2)

from functools import reduce
numbers = [1, 2, 3, 4]
reduce(lambda x, y: x * y, numbers)

"""def sum(x):
    return(lambda a: x+a)

t = sum(5)
print(t(5))
f = sum(20)
print(f(10))

print("-----normal Lambda function-----")

x = lambda a: a * 10
print(x(5))"""

