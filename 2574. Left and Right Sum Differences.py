class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        leftSum = []
        rightSum = []
        length = len(nums)
        for i in range(length):
            if i == 0:
                leftSum.append(0)
            else:
                llist = nums[:i]
                leftSum.append(sum(llist))

            if i == length:
                rightSum.append(0)
            else:
                rlist = nums[i+1:]
                rightSum.append(sum(rlist))


            answer.append(abs(leftSum[i] - rightSum[i]))

        return answer
    
    #https://leetcode.com/problems/left-and-right-sum-differences/