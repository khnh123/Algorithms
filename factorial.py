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
