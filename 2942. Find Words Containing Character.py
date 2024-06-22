class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        y = 0
        for st in words:
            st_set = set(st)
            if x in st_set:
                out.append(y)
                y += 1
            else:
                y += 1
        return out
#https://leetcode.com/problems/find-words-containing-character/