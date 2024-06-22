class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = set()
        for path in paths:
            destinations.add(path[1])  # 도착지를 destinations 집합에 추가
        for path in paths:
            if path[0] in destinations:
                destinations.remove(path[0])  # 출발지가 destinations 집합에 있으면 제거
        return destinations.pop()  # 마지막으로 남은 도착지 반환
#https://leetcode.com/problems/destination-city/