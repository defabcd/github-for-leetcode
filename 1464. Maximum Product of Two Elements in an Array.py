class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 0
        nums.sort(reverse = True)
        answer = (nums[0]-1) * (nums[1]-1)
        return answer


#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/