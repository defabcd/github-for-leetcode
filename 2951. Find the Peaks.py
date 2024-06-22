class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        for i in range(len(mountain)-2):
            if mountain[i] < mountain[i+1] and mountain[i+1] > mountain[i+2]:
                answer.append(i+1)

        return answer
#https://leetcode.com/problems/find-the-peaks/