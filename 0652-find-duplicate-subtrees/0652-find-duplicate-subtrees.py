from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        subs = defaultdict(list)
        res = []
        def dfs(n: TreeNode) -> str:
            if not n:
                return "#"
            s = ",".join([str(n.val), dfs(n.left), dfs(n.right)])
            # print(f'for node with val {n.val} => {s}')
            if len(subs[s]) == 1:
                res.append(n)
            subs[s].append(n)
            return s
        dfs(root)
        return res 