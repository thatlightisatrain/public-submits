def factorial_of(x):
    total = 1
    for i in range(1, x + 1):
        total = total * i
    return total

print(factorial_of(4))