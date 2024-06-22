class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = {}
        
        for idx, char in enumerate(s):
            if char in seen:
                return char
            seen[char] = idx
        
        return ''  
    #https://leetcode.com/problems/first-letter-to-appear-twice/