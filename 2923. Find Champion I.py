class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Iterate through each team
        for team in range(n):
     
            for opponent in range(n):
                if team != opponent and grid[opponent][team] == 1:
                    is_champion = False
                    break
            

            if is_champion:
                return team
        return -1
#https://leetcode.com/problems/find-champion-i/