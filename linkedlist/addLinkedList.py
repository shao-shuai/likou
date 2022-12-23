# Add 2 linked lists
#https://leetcode.com/problems/add-two-numbers/description/

from linked.linkedclass import Node

a = Node(2)
aa = a
for i in [4, 3]:
    aa = aa.addNode(i)

b = Node(5)
bb = b
for j in [6, 4]:
    bb = bb.addNode(j)

def add(l0, l1):
    dummy = Node(-1)
    head = dummy
    carry = 0

    while l0 or l1 or carry:
        curDigit = carry
        if l0:
            curDigit += l0.val
            l0 = l0.next
        if l1:
            curDigit += l1.val
            l1 = l1.next

        head.next = Node(curDigit % 10)
        head = head.next

        carry = curDigit // 10

    return dummy.next

newList = add(a, b)
while newList:
    print(newList.val)
    newList = newList.next