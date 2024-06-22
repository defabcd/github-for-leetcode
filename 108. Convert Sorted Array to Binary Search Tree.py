class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 재귀 함수 정의
        def convert(left, right):
            if left > right:
                return None

            # 중간 요소를 선택하여 노드를 생성
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # 왼쪽과 오른쪽 서브트리를 재귀적으로 생성
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node

        # 전체 배열을 대상으로 재귀 함수 호출
        return convert(0, len(nums) - 1)
    #https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/