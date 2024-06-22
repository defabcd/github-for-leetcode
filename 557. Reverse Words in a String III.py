class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words back together with a space
        reversed_sentence = ' '.join(reversed_words)
        
        return reversed_sentence
#https://leetcode.com/problems/reverse-words-in-a-string-iii/