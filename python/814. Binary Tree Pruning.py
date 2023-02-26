# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not (self.pruneTree(root.left)):
            root.left = None
        if not (self.pruneTree(root.right)):
            root.right = None

        if (not (root.left or root.right)) and root.val == 0:
            return None
        else:
            return root