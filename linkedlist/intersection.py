# Find the intersection of 2 linked list

def getInter(a, b):
    nb = set()
    while a:
        nb.add(a)
        a = a.next
    
    while b:
        if b in nb:
            return b
        b = b.next

# This one would not work since cura would make 2 steps if cura is None
# We need to determined to return to the head of another list in a single step, see getInter3
def getInter2(a,b):
    cura, curb = a, b
    while cura != curb:
        if cura == None:
            cura = b
        if curb == None:
            curb = a
        cura = cura.next
        curb = curb.next

    return cura 

def getInter3(a,b):
    cura, curb = a, b
    while cura != curb:
        if cura == None:
            cura = b
        else:
            cura = cura.next

        if curb == None:
            curb = a
        else:
            curb = curb.next

    return cura