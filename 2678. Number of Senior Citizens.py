class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        for i in range(len(details)):
            first_D = int(details[i][11:len(details[i])-2])
            if first_D > 60:
                answer += 1

        return answer
        
    #https://leetcode.com/problems/number-of-senior-citizens/