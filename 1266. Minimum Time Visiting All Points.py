class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)-1):
            count_L = []
            count_L.append(abs(points[i][0] - points[i+1][0]))
            count_L.append(abs(points[i][1] - points[i+1][1]))
            count += max(count_L)

        return count

        
    #https://leetcode.com/problems/minimum-time-visiting-all-points/