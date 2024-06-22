class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct_elements = [elem for elem, count in counter.items() if count == 1]

        if len(distinct_elements) >= k:
            return distinct_elements[k-1]
        else:
            return ""
    #https://leetcode.com/problems/kth-distinct-string-in-an-array/