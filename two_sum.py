# Brute force
def find_two_b(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [i, j]

# Dictionary
def find_two(nums, target):
    dict = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in dict:
            dict[nums[i]] = i
        else:
            return [i, dict[target - nums[i]]]

# Two pointers
def find_two_p(nums, target):
    nums.sort()

    small = 0
    large = len(nums) - 1

    while small < large:
        if nums[small] + nums[large] < target:
            small += 1
        elif nums[small] + nums[large] > target:
            large -= 1
        else:
            return True

a = [3,2,4]
print(find_two_b(a, 6))
