# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return TreeNode(val)
        if root.val < val:
            if root.right:
                self.insertIntoBST(root.right,val)
                return  root
            else:
                root.right = TreeNode(val)
                return root 
        else:
            if root.left:
                self.insertIntoBST(root.left,val)
                return root
            else:
                root.left = TreeNode(val)
                return root 

        