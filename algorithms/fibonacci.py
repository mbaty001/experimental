from functools import cache
from performance_timer_decorator import clock

@clock
def fibonacci(n):
    return sum(range(1, n+1))

@clock
def fibonacci_sequence(n):
    prev, fib_number = 0, 1
    seq = [prev, fib_number]
    for _ in range(2, n+1):
        prev, fib_number = fib_number, prev + fib_number
        seq.append(fib_number)
    print(seq)
    return fib_number

fibonacci(10)
fibonacci_sequence(10)