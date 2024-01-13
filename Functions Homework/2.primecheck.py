def primecheck(x):
    if x > 1:
        for i in range(2, int(x**0.5) + 1):
            if (x % i) == 0:
                print("This is NOT a prime!")
                return False
        print("This is a prime!")
        return True
    else: return False

print(primecheck(7))