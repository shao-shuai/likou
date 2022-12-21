# Convert a sorted list into a balanced binary search tree resursively

# Construct a binary search tree
from tree.treeclass import Node
from tree.treeclass import inorder

root = Node(8)
left = root.addLeft(3)
right = root.addRight(10)
left_left = left.addLeft(1)
left_right = left.addRight(6)
left_right.addLeft(4)
left_right.addRight(7)
right_right = right.addRight(14)
right_right.addLeft(13)

# inorder traverse of a binary search tree would result in a sorted list
# inorder(root)

def buildBST(nums):
    if len(nums) == 0:
        return None

    mid = len(nums) // 2

    root = Node(nums[mid])
    root.left = buildBST(nums[:mid])
    root.right = buildBST(nums[mid + 1:])

    return root

nums = [1,4,5,6,9,10,13,16,22]
root = buildBST(nums)
inorder(root)