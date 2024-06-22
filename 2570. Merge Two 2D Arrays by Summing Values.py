class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        value_map = {}
        

        for id1, val1 in nums1:
            value_map[id1] = val1
        
        for id2, val2 in nums2:
            if id2 in value_map:
                value_map[id2] += val2
            else:
                value_map[id2] = val2
    
        result = [[id, val] for id, val in value_map.items()]
   
        result.sort()
        
        return result
#https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/