from functools import cache # this would speed it up immensely for more recursion depth
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            l = "" if (not root.right and not root.left) else f"({self.tree2str(root.left)})"
            r = f"({self.tree2str(root.right)})" if root.right else ""
            return f"{root.val}{l}{r}"
        return ""
