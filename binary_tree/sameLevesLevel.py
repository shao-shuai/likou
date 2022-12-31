from tree.treeclass import Node
from tree.treeclass import preorder

root = Node(1)
left = root.addLeft(2)
right = root.addRight(3)
left.addLeft(4)
left.addRight(5)
right.addLeft(6)
aa = right.addRight(7)
# aa.addLeft(11)
# aa.addRight(12)




def sameLevesLevel(root):
    d = set()
    def dfs(root, cur):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            d.add(cur)

        dfs(root.left, cur + 1)
        dfs(root.right, cur + 1)

    dfs(root, 0)

    if len(d) == 1:
        return True
    else:
        return False

print(sameLevesLevel(root))
    