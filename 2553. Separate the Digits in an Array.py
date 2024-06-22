class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            element = str(nums[i])
            for j in range(len(element)):
                answer.append(int(element[j]))
        return answer
        
    #https://leetcode.com/problems/separate-the-digits-in-an-array/