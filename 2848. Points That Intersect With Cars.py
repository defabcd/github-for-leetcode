class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        answer = 0
        answer_L = []
        for i, j in nums:
            answer_N = list(range(i, j+1))
            answer_L += answer_N
        a = set(answer_L)
        return len(a)
#https://leetcode.com/problems/points-that-intersect-with-cars/