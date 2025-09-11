class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def solve(root, level):
        	if root:
        		if len(res)==level:
        			res.append(root.val)
        		solve(root.right, level + 1)
        		solve(root.left, level + 1)
        	return 

        res = []
        solve(root,0)
        return res



        # final Solution
        # Helper function "solve" to traverse binary tree recursively
        # if the current node exists, if first time visiting the level, append the node's value to res. 
        # the function recurses to the right child first then the left child, both at the next level. 