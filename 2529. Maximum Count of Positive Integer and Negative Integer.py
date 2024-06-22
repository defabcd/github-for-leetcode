class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_nums = []
        pos_nums = []

        for num in nums:
            if num < 0:
                neg_nums.append(num)
            elif num > 0:
                pos_nums.append(num)
        

        return max(len(neg_nums), len(pos_nums))
#https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/