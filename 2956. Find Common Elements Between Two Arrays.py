class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        count1 = 0
        count2 = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count1 += 1
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                count2 += 1
        output = [count1, count2]
        return output
#https://leetcode.com/problems/find-common-elements-between-two-arrays/