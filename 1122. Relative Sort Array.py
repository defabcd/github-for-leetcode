class Solution:
    from collections import Counter
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        answer = []

        for num in arr2:
            answer.extend([num] * count.pop(num, 0))

        rest = sorted(count.elements())
        answer.extend(rest)
        
        return answer
#https://leetcode.com/problems/relative-sort-array/