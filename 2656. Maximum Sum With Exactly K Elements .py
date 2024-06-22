class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum_L = []
        max_N = max(nums)
        for i in range(k):
            sum_L.append(max_N)
            max_N += 1

        return sum(sum_L)

        
    #https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/