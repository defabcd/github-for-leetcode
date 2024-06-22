import numpy as np



class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = np.array(nums).reshape((-1, 1)) # (n,1)
        B = np.array(nums).reshape((1, -1)) # (1,n)
        C = np.abs(A - B) # (n, n)
        out = np.sum(C == k)
        if k != 0:
            return out//2
        else:
            (out - n) // 2
    #https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/