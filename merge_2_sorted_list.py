def merge(a, b):
    # Create an empty list
    res = []

    pt1 = 0
    pt2 = 0

    while pt1 < len(a) and pt2 < len(b):
        if a[pt1] < b[pt2]:
            res.append(a[pt1])
            pt1 += 1
        else:
            res.append(b[pt2])
            pt2 += 1

    while pt1 < len(a):
        res.append(a[pt1])
        pt1 += 1

    while pt2 < len(b):
        res.append(b[pt2])
        pt2 += 1

    return res
    



a = [1,3,5,7,9]
b = [2,4,6,8]
e = [1,2,3]
f = [100, 200, 300]
c = merge(a, b) # c is [1,2,3,4,5,6,7,8,9]
g = merge(e, f)
print(c)
print(g)