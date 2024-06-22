class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Step 1: Count frequencies of each character
        freq = Counter(s)
        
        # Step 2: Check if all frequencies are the same
        values = list(freq.values())
        return all(value == values[0] for value in values)
    #https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/