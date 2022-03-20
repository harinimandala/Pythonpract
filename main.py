from functools import reduce
import math
numbers = [1, 2, 3]
reduce(lambda x, y: x + y, numbers)

x = (12, 90, 98)
y = (56, 90, 100)

print(min(x))
print(max(y))
