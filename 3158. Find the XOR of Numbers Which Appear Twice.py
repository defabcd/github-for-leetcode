class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen_twice = set()
        result = 0
        
        for num in nums:
            if num in seen_twice:
                result ^= num
            else:
                seen_twice.add(num)
        
        return result
#https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/