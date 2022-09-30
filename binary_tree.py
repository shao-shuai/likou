# inspired by https://www.youtube.com/watch?v=6oL-0TdVy28

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a new tree with a
# command + shift + l
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

#       1
#      /\
#     2  3
#    /\  /\
#   4 5 6  7

# it would be convenient to convert a list into a binary tree

# preorder traversal of binary tree
def preorder_print(start, traversal):
    if start:
        traversal += (str(start.value)) + "->"
        traversal = preorder_print(start.left, traversal)
        traversal = preorder_print(start.right, traversal)

    return traversal

# inorder traversal of binary tree
def inorder_print(start, traversal):
    if start:
        traversal = inorder_print(start.left, traversal)
        traversal += (str(start.value)) + "->"
        traversal = inorder_print(start.right, traversal)

    return traversal

# postorder traversal of binary tree
def postorder_print(start, traversal):
    if start:
        traversal = postorder_print(start.left, traversal)
        traversal = postorder_print(start.right, traversal)
        traversal += (str(start.value)) + "->"

    return traversal


print(preorder_print(tree, ""))
print(inorder_print(tree, ""))
print(postorder_print(tree, ""))