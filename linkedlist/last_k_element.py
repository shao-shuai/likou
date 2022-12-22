from linked.linkedclass import Node

a = Node(-1)
p = a
for i in range(10):
    p = p.addNode(i)

# 1->2->3->4->4->4->5
c = Node(1)
d = d = c
d = d.addNode(2)
d = d.addNode(3)
d = d.addNode(4)
d = d.addNode(4)
d = d.addNode(4)
d = d.addNode(5)

def kth(head, k):
    p = head
    for i in range(k):
        p = p.next

    while p:
        p = p.next
        head = head.next

    return head

print(kth(a, 2).val)