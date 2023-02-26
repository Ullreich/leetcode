# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # init the dict
        dic_of_vals = dict()

        iterate_through(root, 0, 0, dic_of_vals)

        # iterate over keys and return as list
        return [[j[0] for j in sorted(dic_of_vals[i],  key=lambda x: x[::-1])] for i in sorted(dic_of_vals.keys())]


def iterate_through(node, index, depth, dic_of_vals,):
    # check if key is in the dic, else new list
    if index in dic_of_vals.keys():
        #for ind, tup in zip(range(len(dic_of_vals[index])), dic_of_vals[index]):
        #    if tup
        dic_of_vals[index].append([node.val, depth])
    else:
        dic_of_vals[index]=[[node.val, depth]]
    # run on function with index to the left
    if node.left:
        iterate_through(node.left, index - 1, depth + 1, dic_of_vals)
    if node.right:
        iterate_through(node.right, index + 1, depth + 1, dic_of_vals)