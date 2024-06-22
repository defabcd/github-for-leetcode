class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                count = nums[i]
                break
        return count
        
    #https://leetcode.com/problems/n-repeated-element-in-size-2n-array/