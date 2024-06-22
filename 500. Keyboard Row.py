class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        answer = []
        s_L = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for i in words:
            n = len(i)
            lis = str
            count = 0
            if i[0].lower() in s_L[0]:
                lis = s_L[0]
            elif i[0].lower() in s_L[1]:
                lis = s_L[1]
            elif i[0].lower() in s_L[2]:
                lis = s_L[2]
            for j in i:
                if j.lower() in lis:
                    count += 1
            if count == n:
                answer.append(i)

        return answer
#https://leetcode.com/problems/keyboard-row/