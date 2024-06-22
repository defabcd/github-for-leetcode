class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        answer = 0
        digit_RealSum = sum(nums)
        digit_Sum = 0
        digit_Sum_List = []
        for i in range(len(nums)):
            nums_Element = nums[i]
            while nums_Element > 0:
                digit = nums_Element % 10
                digit_Sum_List.append(digit)
                nums_Element //= 10

        digit_Sum = sum(digit_Sum_List)
        answer = abs(digit_Sum - digit_RealSum)
        return answer

#https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/