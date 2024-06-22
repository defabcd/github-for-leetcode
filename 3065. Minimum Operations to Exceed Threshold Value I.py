class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[0] < k:
                nums.pop(0)
                answer += 1
        
        return answer
    
    #https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/