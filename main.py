# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
            if root:
                return [i for i in self.inorderTraversal(root.left)] + [root.val] + [i for i in self.inorderTraversal(root.right)]
            return []

test = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(1, TreeNode(4))))

a = Solution()
print(a.inorderTraversal(test))