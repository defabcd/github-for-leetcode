class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        position = {}
        
        for index, char in enumerate(s):
            if char in position:
                first_index = position[char]
                required_distance = distance[ord(char) - ord('a')]
                actual_distance = index - first_index - 1
                if actual_distance != required_distance:
                    return False
            else:
                position[char] = index
                
        return True
#https://leetcode.com/problems/check-distances-between-same-letters/