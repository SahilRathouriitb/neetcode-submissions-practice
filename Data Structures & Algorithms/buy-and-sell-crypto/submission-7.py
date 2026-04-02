class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
      b = 0 
      max_profit = 0

      for s in range(0,len(prices)):

            max_profit = max(max_profit,prices[s]-prices[b])
            
            if (prices[s]-prices[b]) < 0:
                b = s

      if max_profit <= 0:
        return 0
      else:
        return max_profit

      