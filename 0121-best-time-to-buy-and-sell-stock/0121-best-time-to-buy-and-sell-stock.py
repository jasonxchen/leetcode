class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            sell += 1
        return max_profit
        