#
# https://leetcode.com/problems/delete-node-in-a-bst/
#
# Given a root node reference of a BST and a key, delete the node 
# with the given key in the BST. Return the root node reference (possibly updated) 
# of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node. 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "86 ms",
    "fasterThan": "85%",
    "memory": "18.5 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        nd, nd_p, branch = find_node(root, key)
        if nd == None:
            return root
        
        pre, pre_p = find_pre(nd)
        post, post_p = find_post(nd)
        #print(to_str(nd), to_str(nd_p), branch, to_str(pre), to_str(pre_p), to_str(post), to_str(post_p))
        #br()

        if nd.left == None and nd.right == None:
            if nd_p != None:
                if branch == 'left':
                    nd_p.left = None
                elif branch == 'right':
                    nd_p.right = None 
                else:
                    assert False
                return root

            else:
                return None

        if post != None:
            if post_p != nd:
                post_p.left = post.right

            if nd_p != None:
                if branch == 'left':
                    nd_p.left = post
                elif branch == 'right':
                    nd_p.right = post
                else:
                    assert False
            else:
                root = post

            post.left = nd.left
            if post != nd.right:
                post.right = nd.right

        elif pre != None:
            if pre_p != nd:
                pre_p.right = pre.left

            if nd_p != None:
                if branch == 'left':
                    nd_p.left = pre
                elif branch == 'right':
                    nd_p.right = pre
                else:
                    assert False
            else:
                root = pre

            if nd.left != pre:
                pre.left = nd.left
            #br()

        else:
            return None

        return root

def find_node(root, key):
    nd = root
    parent = None
    branch = None
    while True:
        if nd == None:
            return None, None, None

        if nd.val == key:
            return nd, parent, branch
        elif key < nd.val:
            parent = nd
            branch = 'left'
            nd = nd.left 
        else:
            parent = nd
            branch = 'right'
            nd = nd.right 

    return None, None, None

def find_pre(nd):
    if nd.left == None:
        return None, None

    parent = nd
    nd = nd.left
    while True:
        if nd.right == None:
            break

        parent = nd
        nd = nd.right

    return nd, parent

def find_post(nd):
    if nd.right == None:
        return None, None

    parent = nd
    nd = nd.right
    while True:
        if nd.left == None:
            break

        parent = nd
        nd = nd.left 

    return nd, parent

def to_str(nd):
    if nd == None:
        nd_v = None
    else:
        nd_v = nd.val 

    return '%s' % nd_v








