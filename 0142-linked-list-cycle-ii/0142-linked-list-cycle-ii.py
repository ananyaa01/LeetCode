# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        start=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while(slow!=start):
                    slow=slow.next
                    start=start.next
                return start
        return None    
        