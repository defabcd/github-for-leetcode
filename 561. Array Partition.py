class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(int(len(nums)/2)):
            answer += nums[i*2]

        return answer
        #https://leetcode.com/problems/array-partition/