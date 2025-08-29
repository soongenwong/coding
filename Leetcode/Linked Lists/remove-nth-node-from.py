# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
        


        # initial plan
        # this is linked list. use fast, slow, head, val and next
        # count from the back and remove the nth position. 

        # final solution
        # move the fast pointer n steps forward.
        # edge case: if n is the last node from the back, continue to the second last node from the back. 
        # move both fast and slow one step at a time
        # slow is just before the node to be removed
        # skip the target node