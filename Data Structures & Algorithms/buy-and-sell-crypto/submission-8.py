class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minPrice = 0, prices[0]
        for curr in prices:
            profit = max(profit, curr - minPrice)
            minPrice = min(minPrice, curr)

        return profit