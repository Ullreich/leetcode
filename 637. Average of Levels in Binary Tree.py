# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret_list = list()
        depth = [root]

        while depth:
            ret_list.append(sum([i.val for i in depth]) / len(depth))
            depth = [i.left for i in depth if i.left] + [i.right for i in depth if i.right]

        return ret_list