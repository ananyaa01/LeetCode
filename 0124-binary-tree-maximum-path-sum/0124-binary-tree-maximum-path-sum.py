# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[float('-inf')]
        self.maxPath(root,maxi)
        return maxi[0]
    def maxPath(self,node,maxi):
        if not node:
            return 0
        ls=max(0,self.maxPath(node.left,maxi))
        rs=max(0,self.maxPath(node.right,maxi))
        data=node.val
        maxi[0]=max(maxi[0],ls+rs+data)
        return data + max(ls,rs)
        
        