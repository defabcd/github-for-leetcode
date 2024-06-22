class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        answer = []
        nums.sort(reverse = True)
        for i in range(len(nums)):
            answer.append(nums[i])
            if sum(answer) > sum(nums[i+1:]):
                break
        
        return answer
#https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/