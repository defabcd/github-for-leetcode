class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        
        # 숫자 인덱스를 제거하여 실제 단어를 추출합니다
        actual_words = [word[:-1] for word in words]
        
        # 숫자 인덱스를 기준으로 단어를 정렬합니다
        sorted_words = sorted(zip(actual_words, words), key=lambda x: int(x[1][-1]))
        
        # 정렬된 실제 단어들을 원래 문장으로 연결하여 반환합니다
        reconstructed_sentence = ' '.join([word[0] for word in sorted_words])
        
        return reconstructed_sentence
#https://leetcode.com/problems/sorting-the-sentence/
