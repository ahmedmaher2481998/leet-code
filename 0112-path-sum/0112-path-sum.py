# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.res = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # print(f"target sum {targetSum}")
        if not root:
            return False
        if targetSum == root.val and not root.left and not root.right:
            return True
        newSum = targetSum - root.val
        l = self.hasPathSum(root.left, newSum)
        r = self.hasPathSum(root.right, newSum)
        # print(f"n: {root.val} , l {l} ,r {r},sum:{targetSum}")
        return (r or l)
