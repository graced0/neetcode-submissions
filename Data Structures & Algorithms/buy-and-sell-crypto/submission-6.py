class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high

        #keep track of the lowest price, recalculate max profit each loop
        max_profit, min_price = 0, prices[0]
        for curr_price in prices:
            max_profit = max(max_profit, curr_price - min_price)
            min_price = min(min_price, curr_price)

        return max_profit

