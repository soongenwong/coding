# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node





        # initial plan
        # linked list question, use temp and node

        # final solution
        # while head: loop continues as long as there are nodes left in the original list. 
        # temp = head.next : stores the next node
        # head.next = node: reverse the node's pointer to the back
        # node = head : move node forward
        # head = temp : advances head to the next node


        