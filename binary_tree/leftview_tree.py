from tree.treeclass import Node
from tree.treeclass import preorder
from collections import deque

a = Node(4)
a_left = a.addLeft(2)
a.addRight(7)
a_left.addLeft(1)
a_left.addRight(3)

def left_view(root):
    if root is None:
        return []
    
    ans = []
    q = deque([root])

    while len(q) > 0:
        sz = len(q)
        ans.append(q[0].val)
        for _ in range(sz):
            cur = q.popleft();
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return ans

print(left_view(a))