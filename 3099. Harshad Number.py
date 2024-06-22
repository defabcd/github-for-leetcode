class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Convert x to string to iterate over digits
        str_x = str(x)
        
        # Calculate sum of digits
        sum_digits = sum(int(digit) for digit in str_x)
        
        # Check if x is a Harshad number
        if x % sum_digits == 0:
            return sum_digits
        else:
            return -1
    #https://leetcode.com/problems/harshad-number/