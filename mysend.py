
from functools import reduce

lis = [i for i in range(1, 101)]
a = reduce(lambda x, y: x + y, lis)
print(a)
