from collections import Counter 
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = sum(1 for pos in position if pos % 2 == 0)
        odd_count = len(position) - even_count
        
        return min(even_count, odd_count)
#https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/