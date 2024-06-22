class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        max_bit_length = max(nums).bit_length() if nums else 0
        bit_count = [0] * max_bit_length

        for num in nums:
            for i in range(max_bit_length):
                if num & (1 << i):
                    bit_count[i] += 1

        result = 0
       
        for i in range(max_bit_length):
            if bit_count[i] >= k:
                result |= (1 << i)
        
        return result
#https://leetcode.com/problems/find-the-k-or-of-an-array/