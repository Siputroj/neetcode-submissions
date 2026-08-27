# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find midpoint (stop slow at the end of the first half)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse second half
        second = slow.next
        slow.next = None  # Cut off the first half
        prev, curr = None, second

        # Flip orientation
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Interweave the two halves
        first = head
        second = prev  # prev is the head of the reversed second half

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
      

