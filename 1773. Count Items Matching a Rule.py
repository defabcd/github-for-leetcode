class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        for i in range(len(items)):
            if ruleKey == 'type':
                if items[i][0] == ruleValue:
                    answer += 1
            elif ruleKey == 'color':
                if items[i][1] == ruleValue:
                    answer += 1
            elif ruleKey == 'name':
                if items[i][2] == ruleValue:
                    answer += 1
        return answer

#https://leetcode.com/problems/count-items-matching-a-rule/