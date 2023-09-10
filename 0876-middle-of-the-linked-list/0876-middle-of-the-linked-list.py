# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        c=0
        while(temp!=None):
            c+=1
            temp=temp.next
        t=(c//2)+1
        u=1
        temp=head
        while(temp!=None):
            if(u==t) :
                break
            else:
                temp=temp.next
                u+=1
        return temp  
            
                        