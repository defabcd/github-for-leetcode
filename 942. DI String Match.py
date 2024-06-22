class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        left, right = 0, n
        
        for char in s:
            if char == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        
        result.append(left)
        
        return result
#https://leetcode.com/problems/di-string-match/