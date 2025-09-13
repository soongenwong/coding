class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)

    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        
        left_height, right_height = self.Height(root.left), self.Height(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return - 1
        
        return max(left_height, right_height) + 1


        # final solution 
        # height-balanced means difference in height between left and right subtrees is at most 1
        # "isBalanced" calls the function from height
        # if empty tree, height is 0
        # recursively get the height of left and right subtrees
        # if either subtree is unbalanced or the height difference between left and right is > 1, mark as unbalanced. 
        # if balanced, return the height