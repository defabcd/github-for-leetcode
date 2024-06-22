class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = []
        count = 0

        for i in range(len(mat)):
            sub_Count = mat[i].count(1)
            if count < sub_Count:
                count = sub_Count
                answer = [i, sub_Count]
        if not answer:
            answer = [0, 0]
    
        return answer
#https://leetcode.com/problems/row-with-maximum-ones/