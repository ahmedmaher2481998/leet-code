# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS Solution
        # if not root:
        #     return 0
        # l = self.maxDepth(root.left)
        # r = self.maxDepth(root.right)
        # return max(l,r) + 1 
        # Hash Solution 
        map = {}
        def dfs(n:TreeNode):
            if not n:
                return 0
            if n in map:
                return map[n]
            l = dfs(n.left)
            r = dfs(n.right)
            return 1 + max(l,r)
        return dfs(root)
