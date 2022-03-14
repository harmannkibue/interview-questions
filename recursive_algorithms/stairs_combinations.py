def stairs_combination(n) -> int:
    """
    In a stairs you are allowed to take one,two,three or their combinations
    The function bellow allows to calculate how many possible ways of combinations
    one can make given n the number of stairs
    :param integer n:
    :return integer the number of combinations:
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stairs_combination(n - 1) + stairs_combination(n - 2) + stairs_combination(n - 3)


print(stairs_combination(4))
