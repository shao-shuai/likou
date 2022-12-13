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

# 1->2->3->4->4->4->5
c = Node(1)
d = d = c
d = d.addNode(2)
d = d.addNode(3)
d = d.addNode(4)
d = d.addNode(4)
d = d.addNode(4)
d = d.addNode(5)

def delete_iter(head, val):
    if head is None:
        return None

    if head.val == val:
        return head.next

    prev, cur = head, head.next

    while cur:
        if cur.val == val:
            prev.next = cur.next
            cur = cur.next
        else:
            prev, cur = cur, cur.next

    return head

def delete_recur(head, val):
    if head is None:
        return None

    if head.val == val:
        return delete_recur(head.next, val)

    head.next = delete_recur(head.next,val)

    return head

new = delete_recur(c, 4)
while new:
    print(new.val)
    new = new.next
