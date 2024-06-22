class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        answer = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        for j in range(int(len(nums)/2)):
            answer.append(even[j])
            answer.append(odd[j])

        return answer
#https://leetcode.com/problems/sort-array-by-parity-ii/