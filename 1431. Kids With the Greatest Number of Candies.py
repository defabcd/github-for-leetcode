class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_List = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                bool_List.append(True)
            else:
                bool_List.append(False)

        return bool_List
    #https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/