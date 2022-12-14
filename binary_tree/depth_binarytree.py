from tree.treeclass import Node
from tree.treeclass import preorder

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
aa = right.addRight(7)
aa.addLeft(11)
aa.addRight(12)

def depth(root):

    # watch this condition
    if root is None:
        return 0

    if root.left == None and root.right == None:
        return 1

    left = 1 + depth(root.left)
    right = 1 + depth(root.right)

    return max(left, right)

print(depth(root))