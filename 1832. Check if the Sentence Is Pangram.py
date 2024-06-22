class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Set to store unique letters
        letters_seen = set()
        
        # Traverse each character in the string
        for char in sentence:
            if 'a' <= char <= 'z':  # Check if it's a lowercase letter
                letters_seen.add(char)
                
            # Early exit if all letters are seen
            if len(letters_seen) == 26:
                return True
        
        # After traversing the string, check if all 26 letters are seen
        return len(letters_seen) == 26
#https://leetcode.com/problems/check-if-the-sentence-is-pangram/