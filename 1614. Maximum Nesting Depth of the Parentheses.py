class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0  
        current_depth = 0  

        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1

        return max_depth
#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/