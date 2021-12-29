class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        mx = 0
        for i in range(1,len(prices)):
            profit = prices[i]-buy
            
            if profit > mx:
                mx = profit
            if buy > prices[i]:
                buy = prices[i]
                
        return mx