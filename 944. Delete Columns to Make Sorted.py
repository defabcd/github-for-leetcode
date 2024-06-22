class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_columns = len(strs[0])
        num_rows = len(strs)
        
        unsorted_columns_count = 0
        
        for col in range(num_columns):
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    unsorted_columns_count += 1
                    break
        
        return unsorted_columns_count
#https://leetcode.com/problems/delete-columns-to-make-sorted/submissions/1296177514/