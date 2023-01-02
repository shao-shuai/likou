from tree.treeclass import Node
from collections import deque

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
aa = right.addRight(7)
aa.addLeft(11)
aa.addRight(12)

def bfs(root):
    if root is None:
        return 0

    d = set()

    q = deque([(root, 0)])

    while len(q) > 0:
        p = q.popleft()

        if p[0].left is None and p[0].right is None:
            d.add(p[1])
        
        if p[0].left:
            q.append((p[0].left, p[1] + 1))

        if p[0].right:
            q.append((p[0].right, p[1] + 1))

    return max(d)

print(bfs(root))
    
