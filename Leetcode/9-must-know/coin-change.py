class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0
    
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])

        return min_coins[-1] if min_coins[-1] != amount + 1 else - 1


        # initial plan
        # take all the biggest values. 
        # calculate the complement from the target amount value. 
        
        # final solution
        # dynamic programming approach
        # intitalise min coins for the max amount of coins and values. 
        # the minimum number of coins to make up amount of 0 is 0
        # c is the value of the coin
        # min_coins[i] is the minimum number of coins to make up amount i
        # if min_coins[i] is still amount + 1, it means we couldn't find a solution