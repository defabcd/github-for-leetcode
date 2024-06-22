class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for i in nums:
            if i % 2 == 0:
                count += 1
            if count >= 2:
                return True
        
        return False
        
    #https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/