# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node=ListNode()
        dummy_node.next=head
        fast,slow=dummy_node,dummy_node
        for i in range(1,n+2):
            fast=fast.next
        while(fast!=None):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy_node.next
        
        