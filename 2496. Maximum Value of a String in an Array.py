class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def getLen(s:str) -> int:
            if s.isdigit():
                return int(s)
            else:
                return len(s)
        
        return max(getLen(s) for s in strs)
#https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/