"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        retlist = list()
        nodelist = [root]

        while root and not nodelist == []:
            retlist.append([i.val for i in nodelist])
            nodelist = [j for i in [i.children for i in nodelist if i.children] for j in i]

        return retlist