class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.insert(index[i], nums[i])

        return answer
        
        #https://leetcode.com/problems/create-target-array-in-the-given-order/