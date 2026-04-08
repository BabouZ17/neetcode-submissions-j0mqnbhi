class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = r = 0
        buy = prices[l]

        while r < len(prices):
            while r + 1 < len(prices) and prices[r+1] > prices[r]:
                r += 1
            
            profit += prices[r] - prices[l]
            r += 1
            l = r
        return profit