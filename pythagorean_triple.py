# Brute force
def find_b(nums):
    nb = set()
    for num in nums:
        nb.add(num*num)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]**2 + nums[j]**2 in nb:
                return [i, j]

    return False

a = [3,1,5,7,4]
print(find_b(a))
