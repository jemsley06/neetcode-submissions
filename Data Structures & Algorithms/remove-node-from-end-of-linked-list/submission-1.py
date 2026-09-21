# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        len = 0
        while curr:
            len+=1
            curr = curr.next
        i = len - n
        if i == 0:
            return head.next
        curr = head
        for j in range(i):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
        

        