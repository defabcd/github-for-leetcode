class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_Set = set(nums)
        max_N = -1

        for i in nums_Set:
            if i > 0 and -i in nums_Set:
                max_N = max(max_N , i)

        return max_N
#https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/