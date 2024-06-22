class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a=""
        c=0
        for i in s:
            if i==' ':
                c+=1
            if c==k:
                break
            a+=i
        return a

#https://leetcode.com/problems/truncate-sentence/