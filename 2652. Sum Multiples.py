class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum_divisible = 0
        
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum_divisible += i
                
        return sum_divisible
#https://leetcode.com/problems/sum-multiples/