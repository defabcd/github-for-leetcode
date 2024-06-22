class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = 0
        highest = [0]
        for i in range(len(gain)):
            highest.append(gain[i] + highest[i])
        answer = max(highest)

        return answer

#https://leetcode.com/problems/find-the-highest-altitude/