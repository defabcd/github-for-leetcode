class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                reverse = words[j][::-1]
                if words[i] == words[j] or words[i] == reverse:
                    count += 1
        return count

        
#https://leetcode.com/problems/find-maximum-number-of-string-pairs/