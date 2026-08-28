# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        first = l1
        second = l2
        dummy = ListNode(0)
        curr = dummy
        while first and second:
            res = first.val + second.val
            if carry:
                res = res + 1

            if res >= 10:
                carry = True
                res = res % 10
            else:
                carry = False
    
            curr.next = ListNode(res)
            first = first.next
            second = second.next
            curr = curr.next

        while second:
            res = second.val
            if carry:
                res = res + 1
            
            if res >= 10:
                res = res % 10
                carry = True
            else:
                carry = False
            curr.next = ListNode(res)
            second = second.next
            curr = curr.next

        while first:
            res = first.val

            if carry:
                res = res + 1

            if res >= 10:
                res = res % 10
                carry = True
            else:
                carry = False

            curr.next = ListNode(res)
            first = first.next
            curr = curr.next

        if carry:
            curr.next = ListNode(1)

        return dummy.next
