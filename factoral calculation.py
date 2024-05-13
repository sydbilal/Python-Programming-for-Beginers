def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

num = 5
factorial = calculate_factorial(num)
print("Factorial of {} is:".format(num), factorial)
