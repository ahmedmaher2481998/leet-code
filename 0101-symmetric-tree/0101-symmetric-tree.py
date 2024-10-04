# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def s(l, r) -> bool:
            if not l and not r:
                return True
            if l and r:
                # print(f"l: {l.val},r: {r.val}")
                if l.val == r.val:
                    out = s(l.left, r.right)
                    if not out:
                        return False
                    inner = s(l.right, r.left)
                    if not inner:
                        return False
                    return inner and out
                else:
                    return False
            else:
                return False

        return s(root.left, root.right)
