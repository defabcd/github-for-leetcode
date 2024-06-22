class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        answer = 0
        if len(nums) <= 2:
            answer = -1
        else:
            answer_L = []
            mini = min(nums)
            maxi = max(nums)
            for i in range(len(nums)):
                if nums[i] != mini and nums[i] != maxi:
                    answer_L.append(nums[i])
                    break
            answer = answer_L[0]
        return answer
#https://leetcode.com/problems/neither-minimum-nor-maximum/