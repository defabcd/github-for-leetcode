class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        nums = []
        for i in range(len(sentences)):
            count_Num = sentences[i].count(' ')
            nums.append(count_Num)
        
        outcome = max(nums) + 1


        return outcome

        
        
#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/