from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 첫 번째 단어의 문자 빈도로 초기화합니다.
        common_count = Counter(words[0])
        
        # 나머지 단어들을 반복합니다.
        for word in words[1:]:
            # 현재 단어의 문자 빈도를 가져옵니다.
            word_count = Counter(word)
            # common_count를 업데이트하여 최소 빈도만 유지합니다.
            for char in common_count:
                if char in word_count:
                    common_count[char] = min(common_count[char], word_count[char])
                else:
                    common_count[char] = 0
        
        # common_count에서 최종 빈도를 기반으로 결과를 생성합니다.
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result
#https://leetcode.com/problems/find-common-characters/