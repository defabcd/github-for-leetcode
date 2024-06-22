class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        result = []
        i = 0
        
        while i < n:
            if i + 2 < n and s[i + 2] == '#':

                num = int(s[i:i + 2])
                result.append(chr(ord('a') + num - 1))
                i += 3  
            else:

                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1
        
        return ''.join(result)
#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/