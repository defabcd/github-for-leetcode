

class Solution:
    def countEven(self, num: int) -> int:
        out = 0
        for i in range(1, num + 1):
            if self.is_digit_sum_even(i):  # 수정된 부분
                out += 1
        return out
    
    @staticmethod
    def is_digit_sum_even(i: int) -> bool:
        out = 0
        while i:
            i, residue = i // 10, i % 10
            out += residue
        return not (out % 2)

#https://leetcode.com/problems/count-integers-with-even-digit-sum/