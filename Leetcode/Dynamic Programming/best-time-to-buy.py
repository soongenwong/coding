class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n: 
            return 0
        
        s0, s1, s2 = [0] * n, [0] * n, [0] * n 
        
        s0[0] = 0
        s1[0] = -prices[0] 
        s2[0] = 0 # dummy
        
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[-1], s2[-1])
        

        # final solution
        # s0 is day 0, not holding and not in cooldown
        # s1 is negative profit because you buy the stock.
        # s2 is the cooldown after you sell
        # for i in range(1, n): inclusive of 1 to n - 1
        # s0[i] = best profit if not holding a stock
        # s1[i] = best profit if holding a stock
        # s2[i] = best profit if cooling down
        # return max profit of either not holding or just coming out of cooldown
        # time complexity: O(n), loop through all prices exactly once
        # space complexity: O(n), algorithm uses three arrays of size n (becuase of arrays instead of variables). You have to keep track of the value for every day and each list has n entries. 
        # can be optimised to O(1) space complexity by using variables instead of arrays since we only need the previous values to compute the current values.