class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(n1, n2): # n1:left, n2:right
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
            
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
        
        return is_mirror(root.left, root.right)

        # final solution 
        # helper function "is_mirror"
        # if left and right are empty: true; if only 1 is empty, return false
        # return true for "is mirror" if n1 and n2 are equal, and left of n1 is equal to right of n2, and right of n1 is equal to left of n2
        # return the "is_mirror" function from the root. 