class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:



        answer = []
        nums.sort()
        while nums:
            answer.append(nums.pop(1))
            answer.append(nums.pop(0))
        return answer

#https://leetcode.com/problems/minimum-number-game/