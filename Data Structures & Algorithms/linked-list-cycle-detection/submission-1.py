# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and slow:
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
                else:
                    return False
        return False
            
        