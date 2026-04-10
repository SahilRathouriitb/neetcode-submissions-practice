class Solution:
    def maxProfit(self, prices: List[int]) -> int:
          
      profit = 0 
      minima = prices[0]

      for i in range(1,len(prices)):

        minima = min(prices[i], minima)
        profit = max(profit, (prices[i]-minima))

      return profit 

      