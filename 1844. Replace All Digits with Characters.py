class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)

        s_list = list(s)
        
        for i in range(1, len(s_list), 2):
            s_list[i] = shift(s_list[i - 1], int(s_list[i]))
        
        return ''.join(s_list)
#https://leetcode.com/problems/replace-all-digits-with-characters/