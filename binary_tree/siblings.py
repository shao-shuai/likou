from tree.treeclass import Node
from tree.treeclass import preorder

a = Node(4)
a_left = a.addLeft(2)
a.addRight(7)
a_left.addLeft(1)
a_left.addRight(3)

b = Node(5)
b_right = b.addRight(7)
b.addLeft(1)
b_right.addLeft(6)
b_right.addRight(8)

def find_sibling(root, target):
    sibling = None
    while root:
        if root.val ==target:
            return sibling

        if root.val < target:
            sibling = root.left
            root = root.right
        else:
            sibling = root.right
            root = root.left

    return sibling

print(find_sibling(b, 8).val)

