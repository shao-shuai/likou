# inspired by https://www.youtube.com/watch?v=yC83Kp2xig8&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=39
import random
from re import A

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# construct a binary search tree from a list
n = [12, 18, 5, 13, 29]

def insert(data, cur_node):

    if data < cur_node.value:
        if cur_node.left is None:
            cur_node.left = Node(data)
        else:
            insert(data, cur_node.left)

    if data > cur_node.value:
        if cur_node.right is None:
            cur_node.right = Node(data)
        else:
            insert(data, cur_node.right)

    return cur_node

root = Node(n[0])

for i in n[1:]:
    insert(i, root)

print(root.left.value)
print(root.right.value)
print(root.right.left.value)
print(root.right.right.value)

a = 333
b = a
a = 66
print(a)
print(b)