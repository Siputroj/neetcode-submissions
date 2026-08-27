# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## 2 pointers solution

        # witout pre_head, case will break when head is being removed
        pre_head = ListNode(0, head)

        # left is pointed at n + 1, so that when right is at the None (after the last value), 
        # the left will be located on the value before the deletion
        left = pre_head
        right = head
        for _ in range(0, n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return pre_head.next


        
