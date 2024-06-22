class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        
        count = 0
        last_key = s[0].lower()
        
        for char in s[1:]:
            current_key = char.lower()
            if current_key != last_key:
                count += 1
                last_key = current_key
        
        return count
#https://leetcode.com/problems/number-of-changing-keys/