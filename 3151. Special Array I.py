class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        answer = True
        if len(nums) == 1:
            answer = True
        else:
            for i in range(len(nums) - 1):
                if abs(nums[i] - nums[i+1]) % 2 == 0:
                    answer = False
                    break
        return answer
#https://leetcode.com/problems/special-array-i/