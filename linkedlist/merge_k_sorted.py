# There are 2 methods for merging k sorted linked list
# Method 1: using merge iterating the list of linked lists
# Method 2: divide and conquer

from linked.linkedclass import Node

a = Node(1)
p = a
for i in [3,5,6,10]:
    p = p.addNode(i)

b = Node(2)
q = b
for j in [4,7,11,15,20,100]:
    q = q.addNode(j)

c = Node(9)
r = c
for k in [14,17,19,24,26,29,99]:
    r = r.addNode(k)


def traverse(root):
    while root:
        print(root.val)
        root = root.next


def mergeKlists(lists):
    l = len(lists)

    if l == 0:
        return None

    if l == 1:
        return lists[0]

    if l == 2:
        return merge(lists[0], lists[1])

    mid = l // 2
    left = mergeKlists(lists[:mid])
    right = mergeKlists(lists[mid:])

    return merge(left, right)

def merge(a, b):
    dummy = Node(0)
    cur = dummy

    while a and b:
        if a.val < b.val:
            cur.next = a
            cur = cur.next
            a = a.next
        else:
            cur.next = b
            cur = cur.next
            b = b.next

    if a is not None:
        cur.next = a

    if b is not None:
        cur.next = b

    return dummy.next

test = mergeKlists([a,b,c])
traverse(test)
