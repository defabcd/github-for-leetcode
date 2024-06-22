class Solution:
    def findGCD(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        small = nums[0]
        large = nums[-1]
        div = []
        for i in range(1, small + 1):
            if small % i == 0 and large % i == 0:
                div.append(i)

        div.sort(reverse = True)
        answer = div[0]
        return answer
        #https://leetcode.com/problems/find-greatest-common-divisor-of-array/