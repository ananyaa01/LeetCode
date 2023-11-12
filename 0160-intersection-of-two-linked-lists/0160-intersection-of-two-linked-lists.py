# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # hs=set()
        # temp=headA
        # while(temp):
        #     hs.add(temp)
        #     temp=temp.next
        # temp2=headB
        # while(temp2):
        #     if temp2 in hs:
        #         return temp2
        #     else:
        #         temp2=temp2.next
        # return None
        
        diff=get_diff(headA,headB)
        if diff>0:
            while(diff!=0):
                headA=headA.next
                diff-=1
        else:
            while(diff!=0):
                headB=headB.next
                diff+=1
        while(headA):
            if(headA==headB):
                return headA
            headA=headA.next
            headB=headB.next
        return None
def get_diff(temp1,temp2):
    l1=0
    l2=0
    
    while(temp1 or temp2):
        if temp1:
            l1+=1
            temp1=temp1.next
        if temp2:
            l2+=1
            temp2=temp2.next

    return l1-l2
            