class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for currPrice in prices:
            if currPrice < minPrice:
                minPrice = currPrice
            maxProfit = max(maxProfit, (currPrice - minPrice))
        return maxProfit