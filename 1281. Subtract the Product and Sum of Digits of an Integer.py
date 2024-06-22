class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(str(n))
        
    
        product = 1
        summation = 0

        for digit in digits:
            num = int(digit)  
            product *= num    
            summation += num  
        

        difference = product - summation
        
        return difference
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/