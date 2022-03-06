a = "daBcd"
b = "ABC"


def abbreviation(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    if len(a) < len(b):
        return "NO"
    j = len(b) - 1
    res = []
    n = -1 * len(a)
    print("THE n ", n)
    for i in range(-1, n - 1, -1):
        print("THe i ", i)
        if a[i].upper() == b[j] and j > (len(b) * -1):
            if a[i].islower():
                res.append(a[i])
            j -= 1
        elif a[i].isupper() and a[i].lower() in res:
            res.remove(a[i].lower())
        elif a[i].isupper():
            return "NO"
    return "YES"


print(abbreviation(a, b))
