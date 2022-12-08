class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addNode(self, val):
        newNode = Node(val)
        self.next = newNode
        
        return newNode

a = Node(-1)
p = a
for i in range(10):
    p = p.addNode(i)

# while a:
#     print(a.val)
#     a = a.next

# Fast and slow pointer to find the middle of a linked list
def mid(head):
    slow, fast = head, head

    while fast and fast.next:
        fast= fast.next.next
        slow = slow.next

    return slow

print(mid(a).val)

# 2 approaches to find if there is a cycle in linked list
# 1. hash table
# 2. slow and fast pointers