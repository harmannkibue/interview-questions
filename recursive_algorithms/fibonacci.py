# def fibonacci(n, memo={1: 0, 2: 1}):
#     """
#     This is the memoization solution
#     """
#     if n <= 0:
#         return ("Wrong input")
#     elif n in memo:
#         return memo[n]
#     else:
#         memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#         print("THE memo value iss ", memo)
#     return memo[n]

def fibonacci(n):
    """
    This is the bottom up solution
    """
    if n == 1 or n ==2:
        return 1
    bottom_up = [None]*(n+1)
    bottom_up[0] = 0
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        print(i, bottom_up)
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    print(bottom_up)
    return bottom_up[n]


print(fibonacci(1000))
