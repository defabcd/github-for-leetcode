class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        for i in range(1, len(nums) + 1):
            if i == 1:
                arr1.append(nums[i-1])
            elif i == 2:
                arr2.append(nums[i-1])
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i-1])
                else:
                    arr2.append(nums[i-1])
        return arr1 + arr2
#https://leetcode.com/problems/distribute-elements-into-two-arrays-i/