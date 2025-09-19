class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        
        return curr


        # final solution
        # space optimised solution
        # initialise prev and curr to 1 since there is only 1 way to reach the base cases(0 and 1)
        # update prev and curr by shifting their values
        # curr becomes the sum of the previous 2 values. 
        