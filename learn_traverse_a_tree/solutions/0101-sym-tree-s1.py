#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#

from typing import List
import pdb

solution_json = {
    "date": "2021/3/27"
}

def check_tree_1(root, path):
    #print(root.val)
    if root == None:
        path.append(None)
    else:
        path.append(root.val)
        check_tree_1(root.left, path)
        check_tree_1(root.right, path)

def check_tree_2(root, path):
    if root == None:
        path.append(None)
    else:
        path.append(root.val)
        check_tree_2(root.right, path)
        check_tree_2(root.left, path)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        path1 = []
        check_tree_1(root, path1)
        path2 = []
        check_tree_2(root, path2)
        #pdb.set_trace()
        return path1 == path2 
