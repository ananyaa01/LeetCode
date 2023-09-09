# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack, temp = [], head
 
        while temp:
            stack.append(temp)
            temp = temp.next
 
        if len(stack)>0:
        
            head=temp=stack.pop()

        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next
 
        if temp:
            temp.next = None
            
        
        return head
 
       
        