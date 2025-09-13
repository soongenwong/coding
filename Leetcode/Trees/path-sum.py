class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_sum or right_sum

        


        # final solution 
        # if root is empty, return False
        # if left and right of the root are empty, return True if the taget sum is equal to root value. 
        # recursive call (a function calls itself to solve a smaller instance of the same problem)
        # reduce the target sum by the current node's value for the next recursive call. 
        # return True if either the left or right subtree has a valid path. 
