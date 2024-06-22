class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        difference_1 = list(nums1_set - nums2_set)
        difference_2 = list(nums2_set - nums1_set)
        
        return [difference_1, difference_2]
#https://leetcode.com/problems/find-the-difference-of-two-arrays/