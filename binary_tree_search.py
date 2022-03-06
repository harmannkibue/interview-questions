import math
arr = [1, 4, 5, 8, 2, 9, 13, 3]


class BinarySearch:

    def __init__(self, input, number):
        self.input = sorted(set(input))
        self.number = number
        self.original_arr = input
        self.maximum_traversals = int(math.log2(len(input)))

    def binary_search(self, arr, num, end=0):
        self.input = arr
        len_of_array = len(self.input)

        if end <= self.maximum_traversals:
            self.input = sorted(arr)
            self.number = num
            half_index = int((len_of_array / 2))
            half = self.input[half_index]

            if half == self.number:
                result = ("{} found at index {}".format(self.number, self.original_arr.index(half)))
            elif half > self.number:
                end += 1
                result = (self.binary_search(self.input[:self.input.index(half)], self.number, end))
            else:
                end += 1
                result = (self.binary_search(self.input[self.input.index(half):], self.number, end))
        else:
            result = "Number not found in data"

        return result

a = BinarySearch(arr, 9)
print(a.binary_search(arr, 9))

# [1, 2, 3, 4, 5, 8, 9, 13]
