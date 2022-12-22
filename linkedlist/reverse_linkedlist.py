# Reverse a linkedin both recursively and interatively
from linked.linkedclass import Node

a = Node(-1)
p = a
for i in range(10):
    p = p.addNode(i)

def reverse_recur(head):
    if head == None or head.next == None:
        return head

    n = reverse_recur(head.next)
    head.next.next = head
    head.next = None

    return n

def reverse_iter(head):
    if head == None or head.next == None:
        return head

    prev, cur = None, head

    while cur:
        temp = cur.next
        cur.next = prev
        # prev.next = None
        prev = cur
        cur = temp

    return prev

new = reverse_iter(a)
while new:
    print(new.val)
    new = new.next
