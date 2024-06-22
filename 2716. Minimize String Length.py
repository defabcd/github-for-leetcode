class Solution:
    def minimizedStringLength(self, s: str) -> int:
        a=""
        for i in s:
            if(i not in a):
                a+=i
        return(len(a))
        
        
#https://leetcode.com/problems/minimize-string-length/