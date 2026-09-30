class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for currPrice in prices:
            maxProfit = max(maxProfit, (currPrice - minPrice))
            if currPrice < minPrice:
                minPrice = currPrice
        return maxProfit