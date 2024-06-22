class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []

        max_from_right = -1
        for i in range(n - 1, -1, -1):
            new_max = max_from_right
            max_from_right = max(max_from_right, arr[i])
            arr[i] = new_max

        return arr
#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/