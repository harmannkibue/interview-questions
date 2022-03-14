class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def invert_tree(self, root):
        if root.left:
            original_right = root.right
            root.right = root.left
            root.left = original_right
            root.left.invert_tree(root.left)
            root.right.invert_tree(root.right)
        return self.inorderTraversal(root)


root = Node(4)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(7)
root.insert(6)
root.insert(9)
root.insert(21)

print(root.print_tree())
print(root.inorderTraversal(root))
root.invert_tree(root)
print(root.inorderTraversal(root))

