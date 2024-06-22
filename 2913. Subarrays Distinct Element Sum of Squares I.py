class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(n):
            for j in range(i, n):
                sub_array = nums[i:j+1]
                distinct_count = len(set(sub_array))
                total_sum += distinct_count ** 2
        
        return total_sum        
    #https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/