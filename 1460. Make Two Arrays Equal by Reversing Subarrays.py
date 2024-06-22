class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
         
        return sorted(target) == sorted(arr)
#https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/