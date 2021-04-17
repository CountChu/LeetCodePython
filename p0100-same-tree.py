# 
# Given the roots of two binary trees p and q, write a function to check 
# if they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.
# 

from typing import List
import pdb

#
# Definition for a binary tree node.
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def visit_tree(p, q):
            line = ''
        
            if p == None and q == None:
                return True
        
            if p == None and q != None:
                return False
                
            if p != None and q == None:
                return False
        
            if p.val != q.val:
                return False

            line += 'p.val = %d, q.val = %d, ' % (p.val, q.val)
            print(line)
            
            same = visit_tree(p.left, q.left)
            if not same:
                return False

            same = visit_tree(p.right, q.right)
            if not same:
                return False

            return True        

        same = visit_tree(p, q)
        return same
            

    def build_tree(self, ls):
        idx_node_d = {}
        for i in range(len(ls)):
        
            if i not in idx_node_d:
                node = TreeNode(ls[i])
                idx_node_d[i] = node
            node = idx_node_d[i]    
            
            left_idx = 2*i + 1
            if left_idx >= len(ls):
                left = None
            else:    
                if ls[left_idx] == None:
                    left = None
                else:    
                    left = TreeNode(ls[left_idx])
                idx_node_d[left_idx] = left
        
            right_idx = 2*i + 2
            if right_idx >= len(ls):
                right = None
            else:   
                if ls[right_idx] == None:
                    right = None
                else:
                    right = TreeNode(ls[right_idx])
                idx_node_d[right_idx] = right
            
            if node != None:
                node.left = left
                node.right = right
            
        if len(idx_node_d) == 0:
            return None
        else:
            return idx_node_d[0]    
        

    