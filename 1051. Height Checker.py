class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        corr = sorted(heights)
        for i in range(len(heights)):
            if corr[i] != heights[i]:
                answer += 1
        return answer
#https://leetcode.com/problems/height-checker/