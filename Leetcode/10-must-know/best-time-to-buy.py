class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)
        
        return profit

        # initial plan
        # use hashmap to store values, use stack
        # find the lowest value from the stack.
        # use complement to subtract current value and value in stack.

        # final solution
        # iterate through the prices from the second day
        # if buying price is more than price today, update buying price to price today. 
        # profit is the max between profit, and  p(today's price) and buy price