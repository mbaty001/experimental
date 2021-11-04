import time

# recurent, sloooow
def factorial(n): 
  """returns n!"""
  return 1 if n < 2 else n * factorial(n - 1)

from functools import reduce
from operator import mul

#reduce - nonrecurent - fast
def factorial_reduce(n):
    return reduce(mul, range(1, n+1))

start = time.time()
print(factorial(100))
stop = time.time()
print(stop - start)

start = time.time()
print(factorial_reduce(100))
stop = time.time()
print(stop - start)

