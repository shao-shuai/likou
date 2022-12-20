from tree.treeclass import Node

root = Node(1)
left = root.addLeft(2)
right = root.addRight(2)
left.addLeft(3)
left.addRight(4)
right.addLeft(4)
right.addRight(3)

def isSymmetric(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    return a.val == b.val and isSymmetric(a.left, b.right) and isSymmetric(a.right, b.left)

print(isSymmetric(root.left, root.right))