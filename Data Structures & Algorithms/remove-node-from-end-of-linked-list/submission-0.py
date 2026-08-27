# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # 1. Count total length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # 2. Advance to the node right BEFORE the one to remove
        steps_to_prev = length - n
        prev = dummy
        for _ in range(steps_to_prev):
            prev = prev.next

        # 3. Delete the target node
        prev.next = prev.next.next

        return dummy.next

        