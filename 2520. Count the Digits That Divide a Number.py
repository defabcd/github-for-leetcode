class Solution:
    def countDigits(self, num: int) -> int:
        # Convert num to string
        num_str = str(num)
        
        # Initialize counter
        count = 0
        
        # Iterate through each digit in num_str
        for digit_char in num_str:
            digit = int(digit_char)
            if digit != 0 and num % digit == 0:
                count += 1
        
        return count
#https://leetcode.com/problems/count-the-digits-that-divide-a-number/