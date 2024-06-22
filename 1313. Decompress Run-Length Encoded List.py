class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(int(len(nums)/2)):
            for j in range(nums[2*i]):
                answer.append(nums[2*i+1])

        return answer
    #https://leetcode.com/problems/decompress-run-length-encoded-list/