class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 점수의 길이 n
        n = len(score)
        
        # 점수와 원래 인덱스를 유지하는 리스트 생성
        score_with_indices = [(s, i) for i, s in enumerate(score)]
        
        # 점수를 내림차순으로 정렬
        score_with_indices.sort(reverse=True, key=lambda x: x[0])
        
        # 결과 배열 초기화
        result = [""] * n
        
        # 각 점수에 대해 순위 매핑
        for rank, (s, i) in enumerate(score_with_indices):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)
        
        return result
        
    #https://leetcode.com/problems/relative-ranks/