class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_Code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            morse = ''
            for i in word:
                morse += morse_Code[ord(i)-ord('a')]
            transformations.add(morse)
        return len(transformations)
    
    
#https://leetcode.com/problems/unique-morse-code-words/