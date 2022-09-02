# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        ret_list = list()
        depth = [root]

        while not depth==[]:
            ret_list.append(sum([i.val for i in depth])/len(depth))
            depth = [i.left for i in depth if i.left] + [i.right for i in depth if i.right]

        return ret_list



root = TreeNode(1,(TreeNode(2,None,None)),None)