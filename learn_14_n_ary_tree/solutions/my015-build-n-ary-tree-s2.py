#
# Build a N-ary Tree for the problem 0589.
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
#
# Given an array...
#
# Example 1:
#       Input: ls = [
#           1,
#           None, 3, 2, 4,
#           None, 5, 6
#           ]
#       Output: "1, (3, 2, 4), (5, 6)"
#
# Example 2: 
#       Input: ls = [
#           1,
#           None, 2, 3, 4, 5,
#           None, None, 6, 7, None, 8, None, 9, 10,
#           None, None, 11, None, 12, None, 13, None,
#           None, 14
#       ]
#       Output: "1, (2, 3, 4, 5), (), (6, 7), (8), (9, 10), (), (11), (12), (13), (), (14)"
# 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

'''
        1
    3   2    4 
  5  6      

               1
      2     3     4     5
          6   7   8   9   10
             11  12  13   
             14

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def ls_to_n_ary_tree(self, ls):
        v_ls_ls = []
        v_ls = []
        for v in ls:
            if v != None:
                v_ls.append(v)
            else:
                v_ls_ls.append(v_ls)
                v_ls = []
        if v_ls != []:
            v_ls_ls.append(v_ls)

        v_ls = v_ls_ls.pop(0)
        assert len(v_ls) == 1
        nd = Node(v_ls[0])
        q = [nd]
        head = nd
        while True:
            if q == []:
                break
            if v_ls_ls == []:
                break

            nd = q.pop(0)
            v_ls = v_ls_ls.pop(0)
            children = []
            for v in v_ls:
                children.append(Node(v))
            nd.children = children
            q += children

        return head

    def n_ary_tree_to_str(self, node):
        q = [node]
        out = '%d, ' % node.val
        while True:
            if q == []:
                break

            nd = q.pop(0)
            #print(nd.val)
            if nd.children != None:
                q += nd.children
                out += '('
                for i, child in enumerate(nd.children):
                    if i == len(nd.children) - 1:
                        out += '%d' % child.val
                    else:
                        out += '%d, ' % child.val
                out += '), '

        if out[-2:] == ', ':
            out = out[:-2]
        
        return out
