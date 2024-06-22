class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        out = 0
        for i in range(1, n+1):
            if i % m != 0:
                out += i
            else:
                out -= i
        return out
#https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/