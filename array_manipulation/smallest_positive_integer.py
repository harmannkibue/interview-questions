"""
retung smalled integer greater than 0 given an array

"""

num = [1, 3, 6, 4, 1, 2]


# num = [1, 2, 3]
num = [-1, -3]


def smallest_integer(A: list) -> int:
    """
    :param A:
    :return: smallest integer
    arr less than 100,000
    each element between -1m-1m
    I will return 0 for an invalid input

    """

    # # Here am checking for the constraints provided
    # if len(A) < 100001 and 1000001 > max(A):
    #     N = set(range(1, len(A) + 2))
    #     print(min(set([1, 2, 3]) - set([1, 2, 3, 4, 5])))
    #     return min(N - set(A))
    # else:
    #     # The input is exceeding the contstraints thus invalid
    #     return 0

    if len(A) < 100001 and 1000001 > max(A):
        sorted_list = set(sorted(A))
        print(sorted_list)
        initial = 1
        for i in sorted_list:
            print("THe i iss ", i)
            if i == initial:
                initial += 1
        return initial
    else:
        return 0


print(smallest_integer(num))
