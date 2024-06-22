class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        answer = 0
        num_L = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                num_L.append(nums[i])
        answer = sum(num_L)
        return answer
        
    #https://leetcode.com/problems/sum-of-unique-elements/