# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
            
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2=headA,headB
        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        return l1    
        
#         l1=getCount(headA)
#         l2=getCount(headB)
#         d=0
#         if(l1>l2):
#             d=l1-l2
#             return _getIntersectionNode(d,headA,headB)
#         else:
#             d=l2-l1
#             return _getIntersectionNode(d,headB,headA)
        
# # def _getIntersectionNode(d,head1,head2):
# #     curr1=head1
# #     curr2=head2
# #     for i in range(d):
# #         curr1=curr1.next
# #     while ((curr1 and curr2) !=None):
# #         if(curr1 is curr2) :
# #             return curr1.val
# #         curr1=curr1.next
# #         curr2=curr2.next
# #     return -1    
# # def getCount(node):
# #     temp=node
# #     c=0
# #     while(temp):
# #         c+=1
# #         temp=temp.next
# #     return c  


# def _getIntersectionNode(d,head1,head2):
#     current1=head1
#     current2=head2
#     for i in range(d):
#         if current1 is None:
#             return -1
#         current1=current1.next
#     while current1 is not None and current2 is not None:
#         if current1 is current2:
#             return current1
#         current1=current1.next
#         current2=current2.next
#     return -1
# def getCount(node):
#     cur=node
#     count=0
#     while cur is not None:
#         count+=1
#         cur=cur.next
#     return count
                    
            
            
            
            