class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
        

        # final solution
        # start with the smallest possible value for maxSum
        # if current sum is more than max, max will take current sum value
        # if current sum is less than 0, it won't help to help to increase the max sum.