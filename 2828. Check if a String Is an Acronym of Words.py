class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string_A = ''
        for i in range(len(words)):
            string_A += words[i][0]

        return string_A == s
        
        
        
#https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/