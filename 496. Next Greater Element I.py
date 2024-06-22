class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in nums1:
            idx = nums2.index(i)
            if idx == len(nums2)-1:
                answer.append(-1)
            else:
                for j in range(idx+1,len(nums2)):
                    if nums2[idx] < nums2[j]:
                        answer.append(nums2[j])
                        break
                    if j == len(nums2)-1:
                        answer.append(-1)


        return answer

#https://leetcode.com/problems/next-greater-element-i/