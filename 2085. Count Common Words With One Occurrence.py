from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        count1 = Counter(words1)
        count2 = Counter(words2)

        return sum(1 for i in count1 if count1[i] == 1 and count2[i] == 1)
     
    #https://leetcode.com/problems/count-common-words-with-one-occurrence/   