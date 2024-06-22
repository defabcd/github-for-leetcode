class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        outcome = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1

            outcome.append(count)

        return outcome
        
        
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/