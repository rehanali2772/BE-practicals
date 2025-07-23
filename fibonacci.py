# Global variable to count steps
step_count = 0

def fibonacci(n):
    global step_count
    step_count += 1  # Count every function call
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Driver code
n = int(input("Enter a number: "))
step_count = 0  # Reset step count before calculation
fib_number = fibonacci(n)
print(f"Fibonacci({n}) = {fib_number}")
print(f"Total steps (function calls): {step_count}")
