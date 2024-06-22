class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        non_zero_elements = {num for num in nums if num > 0}

        return len(non_zero_elements)
        
    #https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/