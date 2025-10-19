class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res



        # the difference between the sum of all indices and the sum of all numbers gives the missing number
        # Time complexity: O(N), the for loop iterates over all elements exactly once. 
        # space complexity: O(1), constant number of variables and does not create any new data structures. 
