class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            ele = len(set(nums[:i+1])) - len(set(nums[i+1:]))
            answer.append(ele)
        return answer
#https://leetcode.com/problems/find-the-distinct-difference-array/