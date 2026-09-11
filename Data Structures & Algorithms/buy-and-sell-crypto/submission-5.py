class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        mp = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                if prices[sell] - prices[buy] > mp:
                    mp = prices[sell] - prices[buy]
                sell+=1
            else:
                buy = sell
                sell+=1
        return mp
            
            
            