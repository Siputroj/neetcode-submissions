# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(head, None)
        
    def reverseListHelper(self, node, prev):
        if not node:
            return prev

        temp = node.next
        node.next = prev
    
        return self.reverseListHelper(temp, node)