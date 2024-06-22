class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Check top
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # Check bottom
                    if i == rows - 1 or grid[i+1][j] == 0:
                        perimeter += 1
                    # Check left
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # Check right
                    if j == cols - 1 or grid[i][j+1] == 0:
                        perimeter += 1

        return perimeter
#https://leetcode.com/problems/island-perimeter/