import numpy as np

nums = list(np.random.randint(low=1, high=100, size=10))
print(nums)

# factorial
def factorial(n):
    # Recursion leads to stackoverflow
    if n == 0:
        return 1
    f = 1
    i = 0
    while i < n:
        i += 1
        f = f * i
    return f

from functools import reduce
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
#print(fact(20))

from functools import reduce
from operator import mul
def fact1(n):
    return reduce(mul, range(1, n+1))
#print(fact1(20))
