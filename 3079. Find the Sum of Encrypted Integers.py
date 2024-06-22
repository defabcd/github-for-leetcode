class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i // 10 == 0:
                count += i
            else:
                num_R = []
                for j in range(len(str(i))):
                    num_R.append(int(str(i)[j]))
                ten = len(num_R)
                if ten > 0:
                    best = max(num_R)
                    for k in range(ten):
                        count += best*10**(k)

        return count
#https://leetcode.com/problems/find-the-sum-of-encrypted-integers/
        