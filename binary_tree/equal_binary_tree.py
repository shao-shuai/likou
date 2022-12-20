# To compare if 2 trees are euqal
# First clone the tree -> def clone(root)
# Then invert the cloned tree -> def invert(root)
# Final compare the 2 trees -> def equal(a, b)

from tree.treeclass import Node

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
right.addRight(7)

root2 = Node(1)
left2 = root2.addLeft(2)
right2 = root2.addRight(3)
left2.addLeft(4)
left2.addRight(5)
right2.addLeft(6)
right2.addRight(8)

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

def equal(a, b):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a.val != b.val:
        return False

    return equal(a.left, b.left) and equal(a.right, b.right)
    
copy = clone(root)
print(equal(root, copy))
print(equal(root, root2))