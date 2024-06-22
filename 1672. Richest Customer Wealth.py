class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        acoounts_Count_List = []
        for i in range(len(accounts)):
            acoounts_Count_List.append(sum(accounts[i]))
        ans = max(acoounts_Count_List)
        return ans

        
        
    #https://leetcode.com/problems/richest-customer-wealth/