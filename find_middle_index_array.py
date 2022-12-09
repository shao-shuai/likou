# https://leetcode.com/problems/find-the-middle-index-in-array/description/
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])
        if leftSum == rightSum:
            return 0

        for i in range(1,len(nums)):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        
        return -1
