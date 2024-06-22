class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:

            index = word.index(ch)
           
            reversed_segment = word[:index + 1][::-1]
            result = reversed_segment + word[index + 1:]
        else:
            result = word
        
        return result
#https://leetcode.com/problems/reverse-prefix-of-word/