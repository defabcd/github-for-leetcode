from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        chars_count = Counter(chars)

        for word in words:
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > chars_count[char]:
                    break
            else:
                answer += len(word)
                
        return answer
#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/