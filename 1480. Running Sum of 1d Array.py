class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        outcome = [nums[0]]
        for i in range(len(nums)-1):
            count = outcome[i] + nums[i + 1]
            outcome.append(count)

        return outcome

        
        
#https://leetcode.com/problems/running-sum-of-1d-array/