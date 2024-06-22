class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            if nums.count(i) == 1:
                answer = i
                break

        return answer
#https://leetcode.com/problems/single-number/