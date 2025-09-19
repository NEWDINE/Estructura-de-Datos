from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def serie_fibonacci(n):
    for i in range(n):
        print(fib(i), end=" ")
n = 100000
serie_fibonacci(n)