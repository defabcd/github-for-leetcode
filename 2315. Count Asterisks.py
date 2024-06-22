class Solution:
    def countAsterisks(self, s: str) -> int:

        parts = s.split('|')

        asterisk_count = 0
        
        for i in range(0, len(parts), 2):
            asterisk_count += parts[i].count('*')
        
        return asterisk_count
#https://leetcode.com/problems/count-asterisks/