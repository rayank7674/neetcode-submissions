class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1

        maxprof = 0

        while (i < len(prices) - 1 and j < len(prices)):
            curr = prices[j] - prices[i]
            if curr < 0:
                curr = 0
                if prices[j] < prices[i]:
                    i = j
            j += 1

            if curr > maxprof: 
                maxprof = curr
        
        return maxprof
