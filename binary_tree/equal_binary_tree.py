# To compare if 2 trees are euqal
# First clone the tree -> def clone(root)
# Then invert the cloned tree -> def invert(root)
# Final compare the 2 trees -> def equal(a, b)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addLeft(self, val):
        newNode = Node(val)
        self.left = newNode

        return newNode

    def addRight(self, val):
        newNode = Node(val)
        self.right = newNode

        return newNode

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
right.addRight(7)

def clone(root):
    if root is None:
        return None

    newNode = Node(root.val)
    newNode.left = clone(root.left)
    newNode.right = clone(root.right)

    return newNode

def traverse(root):
    if root is None:
        return None

    print(root.val)
    left = traverse(root.left)
    right = traverse(root.right)

def invert(root):
    if root is None:
        return None

    left = invert(root.left)
    right = invert(root.right)
    root.left = right
    root .right = left

    return root

copy = clone(root)
traverse(root)
traverse(copy)