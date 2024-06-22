class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)
        return answer
#https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/