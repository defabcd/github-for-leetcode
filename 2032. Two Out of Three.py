class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        answer = []
        new_nums1 = list(set(nums1))
        new_nums2 = list(set(nums2))
        new_nums3 = list(set(nums3))
        for i in range(len(new_nums1)):
            if new_nums1[i] in new_nums2 or new_nums1[i] in new_nums3:
                answer.append(new_nums1[i])
        leave = list(set(new_nums2) - set(new_nums1))
        for i in range(len(leave)):
            if leave[i] in new_nums3:
                answer.append(leave[i])
        return answer
#https://leetcode.com/problems/two-out-of-three/