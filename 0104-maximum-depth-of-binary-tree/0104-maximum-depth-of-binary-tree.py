# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        map = {}
        def dfs(n: TreeNode, c: int):
            if not n:
                return
            map[n] = c + 1
            dfs(n.left, c + 1)
            dfs(n.right, c + 1)

        dfs(root, 0)
        if len(map.keys()) > 0:
            ans = sorted(map, key=map.get, reverse=True)[0]
            return map[ans]
        else:
            return 0
