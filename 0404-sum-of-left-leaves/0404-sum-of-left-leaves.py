from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        count = 0
        def isLeaf(n:TreeNode)->bool:
            return not n.left and not n.right
        
        while q:
            n = q.popleft()
            if not n:
                continue
            q.append(n.left) 
            q.append(n.right)
            if n.left and isLeaf(n.left):
                count += n.left.val
        return count

        