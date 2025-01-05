class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        profit = 0
        
        for price in prices:
            if price < minprice:
                minprice = price
            if price - minprice > profit:
                    profit = price - minprice
            
        return profit