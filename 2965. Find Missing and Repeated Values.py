class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        flat_list = [num for row in grid for num in row]

        num_count = [0] * (n * n + 1)
        
        for num in flat_list:
            num_count[num] += 1
        
        a = b = -1
        for i in range(1, n * n + 1):
            if num_count[i] == 2:
                a = i
            elif num_count[i] == 0:
                b = i
        
        return [a, b]
#https://leetcode.com/problems/find-missing-and-repeated-values/