class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_side = 0
        count = 0
  
        for rectangle in rectangles:
            side_length = min(rectangle)
            max_side = max(max_side, side_length)
        
        for rectangle in rectangles:
            side_length = min(rectangle)
            if side_length == max_side:
                count += 1
        
        return count
#https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/