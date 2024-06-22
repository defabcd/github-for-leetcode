class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for i in words:
            front = i[:len(pref)]
            if front == pref:
                answer += 1

        return answer
#https://leetcode.com/problems/counting-words-with-a-given-prefix/