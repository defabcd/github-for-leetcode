from collections import Counter 
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sort_count = Counter(nums)

        answer = sorted(nums, key = lambda x: (sort_count[x], -x))

        return answer
#https://leetcode.com/problems/sort-array-by-increasing-frequency/