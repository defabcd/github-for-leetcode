class Solution:
    def calPoints(self, operations: List[str]) -> int:
        num_L = []
        count = 0
        for i in range(len(operations)):
            if operations[i] == "C":
                num_L.pop(-1)
            elif operations[i] == "D":
                num_L.append(num_L[-1]*2)
            elif operations[i] == "+":
                num_L.append(num_L[-1] + num_L[-2])
            else:
                num_L.append(int(operations[i]))
        if num_L:
            count = sum(num_L)
        else:
            count = 0
        return count
#https://leetcode.com/problems/baseball-game/