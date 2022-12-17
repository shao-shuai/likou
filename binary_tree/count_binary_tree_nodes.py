# We can use both DFS and BFS to count the nodes of binary tree
# https://leetcode.com/problems/count-complete-tree-nodes/description/

from collections import deque

def dqueue_count(root):
    if root is None:
        return 0

    q = deque()
    q.append(root)
    ans = 0
    
    while len(q) > 0:
        p = q.popleft()
        ans += p.val
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)

    return ans

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addLeft(self, val):
        newNode = Node(val)
        self.left = newNode

        return newNode

    def addRight(self, val):
        newNode = Node(val)
        self.right = newNode

        return newNode

root = Node(1)
root.addLeft(2)
right = root.addRight(3)
right.addLeft(4)
right.addRight(5)

print(dqueue_count(root))

    