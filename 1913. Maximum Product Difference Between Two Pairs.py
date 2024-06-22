class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        answer = nums[len(nums)-1]*nums[len(nums)-2] - nums[0]*nums[1]
        return answer

#https://leetcode.com/problems/maximum-product-difference-between-two-pairs/