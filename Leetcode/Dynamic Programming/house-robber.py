class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = max_rob = 0

        for cur_val in nums:
            temp = max(max_rob, prev_rob + cur_val)
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob


        # final solution
        # temp computes the best choice between skipping and robbing the house. 
        # take the max of max_rob and prev_rob + cur_val
        # now, max rob has the value of prev rob
        # temp has the max_rob, best result so far
        # time complexity: O(n), loop through each house exactly once
        # Space complexity: O(1), use a constant amount of variables regardless of input size