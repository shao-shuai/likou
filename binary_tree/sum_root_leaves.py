from tree.treeclass import Node
from tree.treeclass import preorder
from collections import deque

def bfs(root):
    if root is None:
        return 0

    ans = 0

    q = deque([(root, root.val)])
    while len(q) > 0:
        cur, val = q.popleft()
        if cur.left is None and cur.right is None:
            ans += val
        if cur.left:
            q.append((cur.left, val * 10 + cur.left.val))

        if cur.right:
            q.append((cur.right, val * 10 + cur.right.val))

    return ans

def dfs(root, cur):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return cur * 10 + root.val

    a = dfs(root.left, cur * 10 + root.val)
    b= dfs(root.right, cur * 10 + root.val)

    return a + b

a = Node(1)
a_left = a.addLeft(9)
a.addRight(8)
a_left.addLeft(2)

print(dfs(a, 0))
        
