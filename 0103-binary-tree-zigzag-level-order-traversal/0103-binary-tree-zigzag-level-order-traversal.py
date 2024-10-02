from collections import deque
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(1, root)] if root else [])
        seen = defaultdict(int)

        while q:
            lvl, n = q.popleft()

            if n:
                if lvl in seen:
                    seen[lvl].append(n.val)
                else:
                    seen[lvl] = [n.val]
                lvl += 1
                q.append((lvl, n.left))
                q.append((lvl, n.right))
        res = []
        # print(seen)
        for k in seen:
            el = seen[k]
            if k % 2 == 0:
                el.reverse()
            res.append(el)
            # print(el)
        return res
