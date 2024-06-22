class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        outcome = 0
        for i in range(1, len(nums)+1):
            if len(nums) % i == 0:
                outcome += nums[i-1]**2
        return outcome
        
#https://leetcode.com/problems/sum-of-squares-of-special-elements/