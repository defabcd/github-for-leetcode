class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = 0
        nums_T = []
        nums_S = set(nums)
        nums_L = list(nums_S)
        for i in range(len(nums_L)):
            nums_T.append(nums.count(nums_L[i]))
        nums_T.sort(reverse = True)
        for i in range(len(nums_T)):
            if nums_T[0] == nums_T[i]:
                count += nums_T[i]
        return count
    #https://leetcode.com/problems/count-elements-with-maximum-frequency/