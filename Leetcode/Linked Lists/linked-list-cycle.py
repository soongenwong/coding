# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False


        # initial plan
        # check if pos is a valid index in the values in head. 
        # if it is a valid index, return true, else return false. 
    
        # final solution
        # fast pointer moves forward by 2 nodes
        # slow pointer moves forward by 1 node
        # at different speed, the fast pointer will lap the slow pointer. 
        # if the fast and slow pointers met at the same mode, there is a cycle
        