def factorial(n):
    if n > 0:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    elif n == 0:
        return 1
    else:
        return False


print(factorial(-1))
print(factorial(0))
print(factorial(4))
