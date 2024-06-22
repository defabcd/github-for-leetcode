class Solution:
    def alternateDigitSum(self, n: int) -> int:
        out = 0
        op = "+"
        while n:
            n, residue = n//10, n%10
            if op == "+":
                out += residue
                op = "-"
            else:
                out -= residue
                op = "+"
        if op =="+":
            out *= -1

        return out

#https://leetcode.com/problems/alternating-digit-sum/