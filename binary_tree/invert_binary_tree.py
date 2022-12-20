from tree.treeclass import Node
from tree.treeclass import preorder

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
right.addRight(7)

def invert(root):
    if root is None:
        return None

    left = invert(root.left)
    right = invert(root.right)
    root.left = right
    root .right = left

    return root

preorder(root)
inverted = invert(root)
preorder(inverted)
        