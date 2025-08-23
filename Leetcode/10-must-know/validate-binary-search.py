# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        return valid(root, float("-inf"), float("inf"))



        # intial plan
        # use dfs to search for the values. 
        # use hash map to store values. 
        # search all the values to the left of the root node, if it is less, true, else, false.
        # search all the values to the right of the root node, if it is greater, true, else, false. 

        # final solution. 
        # add a helper function "valid"
        # if the node is empty, return true. 
        # check if the node is in between the min and max.
        # left subtree, minimum is the lower bound, and current node is the upper bound.
        # right subree, current node is the lower bound, and maximum is the upper bound. 
        # check from negative infinity to positive infinity. 