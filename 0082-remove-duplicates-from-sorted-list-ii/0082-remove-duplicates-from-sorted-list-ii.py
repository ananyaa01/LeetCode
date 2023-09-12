# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        pre, temp = dummy, head
        while temp:
            if temp.next and temp.next.val == temp.val:
                while temp.next and temp.next.val == temp.val:
                    temp = temp.next
                pre.next = temp.next
            else:
                pre.next = temp
                pre = temp
                # pre=pre.next
            temp = temp.next
        return dummy.next
#         dummy=ListNode(0,next=head)
#         prev=dummy
#         while(head) :
#             if(head == head.next and head.next):
#                 while(head ==head.next and head.next):
#                     head=head.next
#                 prev.next=head.next   
#             else:
#                 prev=prev.next
#             head=head.next    
            
#         return dummy.next
