class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        nums_L = []
        answer = []
        for i in range(len(mat)):
            nums_L.append([i, sum(mat[i])])
        nums_L.sort(key = lambda x:x[0])
        nums_L.sort(key = lambda x:x[1])

        for i in range(k):
            answer.append(nums_L[i][0])
        return answer
        
    #https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/