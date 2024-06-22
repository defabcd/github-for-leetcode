class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = []
        nums_O = nums[:]
        count = 0
        for i in range(len(nums)):
            if nums.count(nums_O[i]) >= 2:
                nums.remove(nums_O[i])
                nums.remove(nums_O[i])
                count += 1
        answer = [count, len(nums)]
        return answer
#https://leetcode.com/problems/maximum-number-of-pairs-in-array/