class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:


        word1_Sum = ''.join(word1)
        word2_Sum = ''.join(word2)

        if word1_Sum == word2_Sum:
            answer = True
        else:
            answer = False
        return answer       
        
        
        
#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/