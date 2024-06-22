class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        start = 0
        
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            
            if balance == 0:

                primitive = s[start:i+1]

                result.append(primitive[1:-1])

                start = i + 1
        
        return ''.join(result)
#https://leetcode.com/problems/remove-outermost-parentheses/