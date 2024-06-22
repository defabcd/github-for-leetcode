class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        
        n = len(nums)
        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        
    
        result = []
        for limit in queries:

            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= limit:
                    left = mid + 1
                else:
                    right = mid - 1
         
            max_size = left
            result.append(max_size)
        
        return result
    #https://leetcode.com/problems/longest-subsequence-with-limited-sum/