class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums.sort()
        
        try:
            start_index = nums.index(target)
        except ValueError:
            return answer  
        
        count = start_index
        while count < len(nums) and nums[count] == target:
            answer.append(count)
            count += 1
            
        return answer
#https://leetcode.com/problems/find-target-indices-after-sorting-array/