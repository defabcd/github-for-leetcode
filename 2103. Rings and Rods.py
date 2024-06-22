class Solution:
    def countPoints(self, rings: str) -> int:
        rod_colors = [set() for _ in range(10)]
        
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rod_colors[rod].add(color)
        
        return sum(len(colors) == 3 for colors in rod_colors)
#https://leetcode.com/problems/rings-and-rods/