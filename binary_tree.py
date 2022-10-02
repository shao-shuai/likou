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

# levelorder traversal of binary tree
def levelorder_print(start, traversal):
    if start is None:
        return

    queue = []
    queue.insert(0, start)
    while len(queue) > 0:
        traversal += str(queue[-1].value) + "->"
        node = queue.pop()
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)

    return traversal

# reverse levelorder traversal of binary tree
def reverse_levelorder_print(start, traversal):
    if start is None:
        return
    
    queue = []
    stack = []
    queue.insert(0, start)
    
    while len(queue) > 0:
        node = queue.pop()
        stack.append(node)

        if node.right:
            queue.insert(0, node.right)
        if node.left:
            queue.insert(0, node.left)
    
    while len(stack) > 0:
        traversal += str(stack.pop().value) + "->"

    return traversal

# calculate height of binary tree
# 1. recursively, refer to preorder, inorder or postorder
# 2. use stack
def tree_height(start):
    if start is None:
        return -1
    left = tree_height(start.left)
    right = tree_height(start.right)

    return 1 + max(left, right)

# calculate size of binary tree recursively
def tree_size(start, size):
    if start:
        size += 1
        size = tree_size(start.left, size)
        size = tree_size(start.right, size)
    
    return size

# calculate size of binary with stack
def tree_size_stack(start):
    if start is None:
        return 0

    stack = []
    stack.insert(0, start)
    size = 1
    while stack:
        node = stack.pop()
        if node.left:
            size += 1
            stack.insert(0, node.left)
        if node.right:
            size += 1
            stack.insert(0, node.right)

    return size

print(preorder_print(tree, ""))
print(inorder_print(tree, ""))
print(postorder_print(tree, ""))
print(levelorder_print(tree, ""))
print(reverse_levelorder_print(tree, ""))
print(tree_height(tree))
print(tree_size(tree, 0))
print(tree_size_stack(tree))