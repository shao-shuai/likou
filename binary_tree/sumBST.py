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

def sumOfBST(a, b, target):
    if a is None or b is None:
        return False

    if a.val + b.val == target:
        return True

    if a.val + b.val < target:
        return sumOfBST(a.right, b, target) or sumOfBST(a, b.right, target)
    else:
        return sumOfBST(a.left, b, target) or sumOfBST(a, b.left, target)

print(sumOfBST(a,b,1))
