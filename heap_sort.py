"""
Implementation of a heap sort given integers.
1.Convert the items given into a max heap
2.Delete items from heap sort and fill another array
"""

arr = [1, 4, 5, 8, 2, 9, 13, 3]

class MaxHeap:

    def __init__(self, arr):
        self.arr = arr
        self.left = None
        self.right = None
        self.sorted_array = []
        self.root = arr[0]

    def create_heap(self):


            

