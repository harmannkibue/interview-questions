class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        """
        :param data:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # def inorder_traversal(self):
