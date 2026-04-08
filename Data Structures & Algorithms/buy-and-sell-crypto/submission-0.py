class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        previous_lowest_price = float("+inf")

        for i in range(len(prices)):
            if prices[i] > previous_lowest_price:
                profits.append(prices[i] - previous_lowest_price)

            previous_lowest_price = min([previous_lowest_price, prices[i]])
        return max(profits)