# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = npn
            prev.next = second

            prev = cur
            cur = npn
        
        return dummy.next
        

        # initial plan
        # use fast, slow, head, next, val
        # swap in pair, then move to next pair

        # final solution
        # npn is next pair node
        # swap second node and current node
        # move to the next pair
        # dummy node is the node before the current node
        