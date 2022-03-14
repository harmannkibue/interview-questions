def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return "Negatives not accepted"


print(factorial(8000000))

4 * 3 * 2 * 1