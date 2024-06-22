class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sort_key(x):
            return (bin(x).count('1'), x)
        return sorted(arr, key = sort_key)
#https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/