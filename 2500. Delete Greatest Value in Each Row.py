class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        
        while grid[0]:
            deleted_values = [max(row) for row in grid]
            
            for i in range(len(grid)):
                grid[i].remove(deleted_values[i])
        
            answer += max(deleted_values)
        
        return answer
#https://leetcode.com/problems/delete-greatest-value-in-each-row/