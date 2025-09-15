from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            
            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels



        # final solution
        # if the root is empty, return []
        # "deque" is a double ended queue. you can append and pop from the left and right ends. 
        # import deque structure
        # a deque is initialised with the tree's root node. 
        # store the lists of values by level, starting with the root. 
        # temporary deque used for children nodes on the next level. 
        # process nodes in the queue until empty
        # remove the leftmost node
        # if the node has left or right children, add them to the temporary queue. 
        # When the current queue is empty and the level is done, add the values of all next-level nodes to the answer. 
        # move to next level by setting Q to temp
        # Reset temp for the next iteration. 
        # return the list of levels