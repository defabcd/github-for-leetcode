class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = 0
        current_chairs = 0
        
        for char in s:
            if char == 'E':
                current_chairs += 1
                max_chairs = max(max_chairs, current_chairs)
            elif char == 'L':
                current_chairs -= 1
        
        return max_chairs
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/