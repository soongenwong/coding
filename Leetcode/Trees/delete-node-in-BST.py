class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root



        # final solution
        # if root is empty, return None
        # if key is less than root value, recurisve call for the function for left side. Search in left subtree. 
        # if key is more than root value, recursive call for the function for right side. search in right subtree. 
        # after you found the key, if the node has no right child, replace it with left child. if node has no left child, replace it with right child
        # if node has both children, move the value from right subtree to deleted value. 
        # left node of right sub tree. 
        # replace with the smallest node in the right sub tree. 
        # delete the in order successor. 

