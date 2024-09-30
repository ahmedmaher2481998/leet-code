from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        bottom = False
        d.append(root)
        while d:
            n = d.popleft()
            if not n:
                bottom = True
                continue
            if bottom:
               return False
            d.append(n.left)
            d.append(n.right)
        return True
