from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code 
        n = len(prices)
        lmin = prices[0]
        lmax = prices[0]
        res = 0
        
        i = 0
        
        while i < n-1:
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            lmin = prices[i]
            
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            lmax = prices[i]
                
            res += ( lmax-lmin )
        return res            