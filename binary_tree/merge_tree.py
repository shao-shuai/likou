from tree.treeclass import Node
from tree.treeclass import preorder

a = Node(1)
a_left = a.addLeft(2)
a_right = a.addRight(3)
a_left.addLeft(4)
a_left.addRight(5)

b = Node(2)
b_left = b.addLeft(6)
b_right = b.addRight(9)
b_right.addLeft(11)
b_right.addRight(20)

def merge_tree(a, b):
    if a is None:
        return b
    
    if b is None:
        return a

    c = Node(a.val + b.val)
    c.left = merge_tree(a.left, b.left)
    c.right = merge_tree(a.left, b.left)

    return c

c = merge_tree(a,b)
preorder(c)