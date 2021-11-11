import functools
import time
from functools import reduce
from operator import mul

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

@clock
def sleeper(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.items())
    time.sleep(kwargs['secs'])

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

@clock
def fibonacci_slowest(n):
    return 1 if n < 2 else fibonacci_slowest(n-2) + fibonacci_slowest(n-1)

@functools.cache
@clock
def fibonacci_slowest_cache(n):
    return 1 if n < 2 else fibonacci_slowest_cache(n-2) + fibonacci_slowest_cache(n-1)

@clock
def factorial_reduce(n):
    return reduce(mul, range(1, n+1))

if __name__ == "__main__":
    sleeper(secs=0.123)
    factorial(6)
    factorial_reduce(6)
    fibonacci_slowest(10)
    fibonacci_slowest_cache(10)