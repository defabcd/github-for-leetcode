class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        count = 0
        x_Num_List = []
        num_List = []
        for i in range(len(points)):
            x_Num_List.append(points[i][0])
        x_Num_List.sort()

        for i in range(len(points) - 1):
            num = x_Num_List[i + 1] - x_Num_List[i]
            num_List.append(num)
        result = max(num_List)
        return result



#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/