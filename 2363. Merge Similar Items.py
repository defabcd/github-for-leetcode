class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_map = defaultdict(int)

        for value, weight in items1:
            weight_map[value] += weight
        for value, weight in items2:
            weight_map[value] += weight
        result = [[value, weight] for value, weight in weight_map.items()]
        result.sort(key=lambda x: x[0])
        
        return result
#https://leetcode.com/problems/merge-similar-items/