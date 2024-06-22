
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        
        # 3x3 부분 행렬의 최대값을 찾아서 maxLocal에 할당
        for i in range(1, n - 1):  # 첫 번째 행과 마지막 행을 제외
            row = []
            for j in range(1, n - 1):  # 첫 번째 열과 마지막 열을 제외
                subgrid = [
                    [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1]],
                    [grid[i][j-1], grid[i][j], grid[i][j+1]],
                    [grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
                ]
                max_val = max(map(max, subgrid))  # 3x3 부분 행렬의 최대값
                row.append(max_val)
            maxLocal.append(row)
        
        return maxLocal
#https://leetcode.com/problems/largest-local-values-in-a-matrix/