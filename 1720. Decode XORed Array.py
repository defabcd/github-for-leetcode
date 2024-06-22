class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded) + 1
        arr = [first]
        for i in range(n - 1):
            arr.append(arr[-1] ^ encoded[i])
        return arr
    
    #https://leetcode.com/problems/decode-xored-array/