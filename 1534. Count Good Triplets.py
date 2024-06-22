class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        outcome_L = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        triple = (arr[i], arr[j], arr[k])
                        outcome_L.append(triple)
        return len(outcome_L)
        
        
#https://leetcode.com/problems/count-good-triplets/