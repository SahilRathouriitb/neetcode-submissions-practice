class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # here we just need to catch the upmoves in the graph
        left = 0
        sum = 0

        while left < len(prices) - 1:

            if prices[left+1] > prices[left]:
                sum = sum + (prices[left+1] - prices[left])
            
            left = left + 1
            
        return sum


        