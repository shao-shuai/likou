def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = int(len(arr) / 2)

    equal = []
    smaller = []
    bigger = []

    for i in arr:
        if i == arr[pivot]:
            equal.append(i)
        elif i < arr[pivot]:
            smaller.append(i)
        else:
            bigger.append(i)

    return quick_sort(smaller) + equal + quick_sort(bigger)

print(quick_sort([12,3,4,1,9,5,100,8]))