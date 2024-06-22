class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize the row and column increment counts
        row_count = [0] * m
        col_count = [0] * n
        
        # Process each index to update the row and column counts
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        # Calculate the number of cells with odd values
        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (row_count[i] + col_count[j]) % 2 != 0:
                    odd_count += 1
        
        return odd_count
#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/