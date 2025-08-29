# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        
        left, right = 0, len(list_vals) - 1
        while left < right and list_vals[left] == list_vals[right]:
            left += 1
            right -= 1
        return left >= right

        # initial plan
        # read from front to back and back to front
        # if they are equal, return true. 

        # final solution
        # store values in the list
        # compare left and right value, if they are different, get out of the while loop. 
        # return True if the pointers have crossed, otherwise return False. 
        