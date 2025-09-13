class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1


        # final solution 
        # height-balanced means difference in height between left and right subtrees is at most 1
        # "isBalanced" calls the function from height
        # if empty tree, height is 0
        # recursively get the height of left and right subtrees
        # if either subtree is unbalanced or the height difference between left and right is > 1, mark as unbalanced. 
        # if balanced, return the height