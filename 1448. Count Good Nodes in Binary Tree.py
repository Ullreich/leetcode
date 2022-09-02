# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return findgood(root, root.val)

def findgood(node: Treenode, max):
    l=node.left
    r=node.right
    b = 0
    if node.val >= max:
        max = node.val
        b = 1
    if l and r:
        return b+findgood(l, max)+findgood(r, max)
    elif l:
        return b+findgood(l, max)
    elif r:
        return b+findgood(r, max)
    return b

"""
#prettier but less readable
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return findgood(root, root.val)

def findgood(node: TreeNode, m):

    if node.left and node.right:
        return (node.val >= m)+findgood(node.left, max(node.val, m))+findgood(node.right, max(node.val, m))
    elif node.left:
        return (node.val >= m)+findgood(node.left, max(node.val, m))
    elif node.right:
        return (node.val >= m)+findgood(node.right, max(node.val, m))
    return int(node.val >= m)
"""