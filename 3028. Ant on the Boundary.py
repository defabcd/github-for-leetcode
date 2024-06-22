class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        return_count = 0
        
        for move in nums:
            position += move
            if position == 0:
                return_count += 1
        
        return return_count
#https://leetcode.com/problems/ant-on-the-boundary/submissions/1296178582/