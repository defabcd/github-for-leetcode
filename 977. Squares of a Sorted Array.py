class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for i in nums:
            new.append(i**2)
        new.sort()
        return new
        
    #https://leetcode.com/problems/squares-of-a-sorted-array/