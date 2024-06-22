class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            num = 0
            if words[i][0] == 'a':
                num += 1
            elif words[i][0] == 'e':
                num += 1
            elif words[i][0] == 'i':
                num += 1
            elif words[i][0] == 'o':
                num += 1
            elif words[i][0] == 'u':
                num += 1

            if words[i][-1] == 'a':
                num += 1
            elif words[i][-1] == 'e':
                num += 1
            elif words[i][-1] == 'i':
                num += 1
            elif words[i][-1] == 'o':
                num += 1
            elif words[i][-1] == 'u':
                num += 1

            if num == 2:
                count += 1
        return count
    #https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/