class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    xor_value = nums[i] ^ nums[j]
                    if xor_value > max_xor:
                        max_xor = xor_value
        
        return max_xor if max_xor != float('-inf') else 0
#https://leetcode.com/problems/maximum-strong-pair-xor-i/