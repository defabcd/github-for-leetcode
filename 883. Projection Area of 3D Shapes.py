class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            count += (len(i) - i.count(0))
            count += max(i)
        
        for i in range(len(grid[0])):
            nums = 0
            for j in range(len(grid)):
                if grid[j][i] > nums:
                    nums = grid[j][i]
            
            count += nums

        return count
#https://leetcode.com/problems/projection-area-of-3d-shapes/