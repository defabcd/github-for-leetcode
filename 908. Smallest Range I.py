class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0

        if nums[len(nums)-1] - nums[0] <= 2*k:
            answer = 0
        else:
            answer = nums[len(nums)-1] - nums[0] - 2*k

        return answer
#https://leetcode.com/problems/smallest-range-i/