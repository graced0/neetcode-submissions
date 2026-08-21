class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]
        for n in range(len(prices)):
            max_profit = max(max_profit, prices[n] - min_price)
            if prices[n] < min_price:
                min_price = prices[n]

        return max_profit

