class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # 재귀 함수를 정의하여 모든 부분집합을 탐색하고 XOR total을 계산합니다.
        def backtrack(index, current_xor):
            if index == len(nums):
                # 부분집합에 대한 XOR total을 반환합니다.
                return current_xor
            # 현재 요소를 부분집합에 포함시키는 경우와 포함시키지 않는 경우를 각각 계산합니다.
            include_current = backtrack(index + 1, current_xor ^ nums[index])
            exclude_current = backtrack(index + 1, current_xor)
            # 두 경우의 XOR total을 합하여 반환합니다.
            return include_current + exclude_current
        # 재귀 함수를 호출하여 결과를 반환합니다.
        return backtrack(0, 0)
#https://leetcode.com/problems/sum-of-all-subset-xor-totals/