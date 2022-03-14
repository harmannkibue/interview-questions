"""
The input
generate([
    [1, 2, 3],
    [4, 5, 6]
]);
The output
[
  '1 4', '1 5', '1 6',
  '2 4', '2 5', '2 6',
  '3 4', '3 5', '3 6'
]
"""

"""
Question: Does it work only with 2 dimensional arrays only or should be scalable
"""


def generate(arr:list) -> list:
    """
    :param arr:
    :return generated list:
    """
    column = len(arr[0])
    new_arr = [[""] * column for _ in range(column)]
    count = 0

    for i in range(column):
        new_count = 0
        # Using this value allows expansion of the list columns
        row = 1 if i < len(arr) else len(arr) - 1
        for j in range(column):
            new_arr[i][j] = '{} {}'.format(arr[0][count], arr[row][new_count])
            new_count += 1
        count += 1
    return new_arr


# Testing the functionality
arr = [
    [1, 2, 3],
    [4, 5, 6],
]

print(generate(arr))
