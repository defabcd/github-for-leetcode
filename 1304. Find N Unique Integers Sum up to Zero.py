class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        return result
#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/