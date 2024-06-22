class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        index_L = [index for index, value in enumerate(s) if value == c]

        for i in range(len(s)):
            lis = []
            for j in index_L:
                lis.append(abs(i-j))
            answer.append(min(lis))
        return answer
        
    #https://leetcode.com/problems/shortest-distance-to-a-character/