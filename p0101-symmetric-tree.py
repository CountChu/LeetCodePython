#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#

from typing import List
import pdb

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
        
    def build_tree(self, ls):
        if len(ls) == 0:
            return None
        
        idx_node_d = {}
        for i in range(len(ls)):
            if i not in idx_node_d:
                node = TreeNode(ls[i])
                idx_node_d[i] = node
            node = idx_node_d[i]
            if node == None:
                continue
            
            left_idx = i*2 + 1
            if left_idx >= len(ls):
                left = None
            else:
                if ls[left_idx] == None:
                    left = None
                else:    
                    left = TreeNode(ls[left_idx])
                idx_node_d[left_idx] = left
                
            right_idx = i*2 + 2
            if right_idx >= len(ls):
                right = None
            else:
                if ls[right_idx] == None:
                    right = None
                else:    
                    right = TreeNode(ls[right_idx])
                idx_node_d[right_idx] = right
        
            node.left = left
            node.right = right
            
        if len(idx_node_d) == 0:
            return None
        else:
            return idx_node_d[0]
        

