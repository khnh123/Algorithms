
def fib():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

for i, f in zip(range(10+1), fib()):
    print('{i:3}: {f:3}'.format(i=i, f=f))

# clockdeco - https://github.com/fuyunliu/fluent-python/blob/master/07-closure-deco/clockdeco.py 
# code from the book "fluent-python"

# Без кэширования
from clockdeco import clock
@clock
def fibonacci(n):
	if n < 2:
		return  n
	return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(6))

# С кэшированием
import functools
from clockdeco import clock
@functools.lru_cache() #
@clock #
def fibonacci(n):
	if n < 2:
		return  n
	return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(6))

# yield
def fib(num):
    a,b = 0,1
    for i in range(0, num):
        yield f'{i+1}: {a}'
        a, b = b, a+ b

[print(i) for i in fib(10)]
