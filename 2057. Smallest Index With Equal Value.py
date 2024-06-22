class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            if i%10 == nums[i]:
                answer = i
                break
        return answer
#https://leetcode.com/problems/smallest-index-with-equal-value/