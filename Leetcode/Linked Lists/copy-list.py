class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]



        # final solution 
        # if input list is empty, return None
        # old_to_new is a dictionary that maps original nodes to their corresponding deep copy nodes. 
        # for each node, create a new node having the same value. 
        # store the mapping in the dictionary. 

        # now, set next and random pointers. 
        # set the next value to the deep copy of curr.next
        # set the random value to the deep copy of curr.random
        # ensure that all next and random pointers point to the copied nodes. 
        # return the head of the new deep-copied list. 
