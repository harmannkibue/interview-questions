def stairs_combination(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stairs_combination(n-1) + stairs_combination(n-2) + stairs_combination(n-3)

print(stairs_combination(4))
