# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],minVal:int=float('-inf'),maxVal:int=float('inf')) -> bool:
        if not root :
            return True 
        if(root.val < minVal or root.val > maxVal):
            return False
        left = self.isValidBST(root.left, minVal,root.val - 1 ) 
        right = self.isValidBST(root.right, root.val + 1, maxVal)
        return left and right 
        