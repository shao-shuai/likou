# Definition of binary tree node and traverse functions
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

def preorder(root):
    if root is None:
        return None

    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
    if root is None:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.val)