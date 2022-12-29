from tree.treeclass import Node

def trim(root, l, r):
    if root is None:
        return None

    if root.val < l:
        return trim(root.right, l, r)
    
    if root.val < r:
        return trim(root.left, l, r)

    root.left = trim(root.left, l, r)
    root.right = trim(root.right, l, r)

    return root



    