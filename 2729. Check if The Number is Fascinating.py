class Solution:
    def isFascinating(self, n: int) -> bool:
        final_str = str(n) + str(2*n) + str(3*n)
        if len(final_str) != 9:
            return False
        return set(final_str) == set([str(i) for i in range(1, 10)])
    
    
#https://leetcode.com/problems/check-if-the-number-is-fascinating/