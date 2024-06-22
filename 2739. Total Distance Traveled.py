class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        out = 0
        while mainTank:
            if mainTank  < 5:
                out += mainTank
                return out * 10
            else:
                out += 5
                mainTank -= 5
                if additionalTank:
                    mainTank += 1
                    additionalTank -= 1
        return out * 10

#https://leetcode.com/problems/total-distance-traveled/