# Implement a Recursive Fibonacci Generator
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# Implement an Iterative Fibonacci Generator
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

#Compare Performance
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

#Implement a Generator Function for Fibonacci Sequence
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

# Implement Memoization for Recursive Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

#Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Example
n = 10
print("Fibonacci sequence up to term", n, ":", fibonacci_sequence(n))

#Implement a function that finds the index of the first Fibonacci number that exceeds a given value.

def find_first_exceeding_value(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

# Create a function that determines if a given number is a Fibonacci number.

def is_fibonacci(n):
    x = (5 * n * n + 4) ** 0.5
    y = (5 * n * n - 4) ** 0.5
    return x.is_integer() or y.is_integer()


# Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio

def calculate_fibonacci_ratio(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    ratios = [fib_sequence[i] / fib_sequence[i - 1] for i in range(2, n)]
    return ratios

def golden_ratio():
    return (1 + 5 ** 0.5) / 2

def observe_fibonacci_ratio_approaching_golden_ratio(n):
    ratios = calculate_fibonacci_ratio(n)
    golden_ratio_value = golden_ratio()
    for ratio in ratios:
        print(f"Ratio: {ratio}, Golden Ratio: {golden_ratio_value}")
        if abs(ratio - golden_ratio_value) < 0.00001:
            return

# Example
observe_fibonacci_ratio_approaching_golden_ratio(10)

