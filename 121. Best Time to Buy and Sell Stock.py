class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices :
            return 0
        lowest_price = prices[0]
        maximum_profit = 0
        for price in prices:
            if price < lowest_price:
                lowest_price  = price
            profit = price - lowest_price
            if profit > maximum_profit:
                maximum_profit = profit
        return maximum_profit