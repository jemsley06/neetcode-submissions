# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [0, 0]
        factor = 1
        while l1:
            num1 += (factor * l1.val)
            l1 = l1.next
            factor *= 10
        factor = 1
        while l2:
            num2 += (factor * l2.val)
            l2 = l2.next
            factor *= 10
        sm = num1 + num2
        sm = str(sm)
        head = ListNode(int(sm[len(sm) - 1]), None)
        curr = head
        for i in reversed(range(len(sm) - 1)):
            curr.next = ListNode(int(sm[i]), None)
            curr = curr.next
        return head
        
        