class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            if not node:
                return 0
            
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            res[0] = max(res[0], left + right)
            
            return max(left, right) + 1
        
        res = [0]
        diameter(root, res)
        return res[0]

        



        # final solution 
        # recursively computes the depths of the left and right subtrees. 
        # update the overall maximum diameter. 
        # start from the lowest node and move up 1 level by 1 level. 
        # update the legth of the node to the parent node. 
        # calculate the diameter.