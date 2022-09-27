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
    "date": "2022/9/26",
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

def build_nd_ls(ls):
    ns_ls = []
    for v in ls:
        nd = Node(v)
        ns_ls.append(nd)
    return ns_ls

def str_nd_ls(nd_ls):
    s = ''
    for nd in nd_ls:
        s += '%d, ' % nd.val 
    return s

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def ls_to_n_ary_tree(self, ls):
        v_ls = []
        q = []
        nd = None
        head = None
        for v in ls:
            print('v = %s' % str(v))
            if v == None:
                print('v_ls = %s' % v_ls)
                nd_ls = build_nd_ls(v_ls)
                q += nd_ls
                print('q = %s' % str_nd_ls(q))
                if nd == None:
                    nd = q.pop(0)
                    head = nd
                else:
                    nd.children = nd_ls
                    nd = q.pop(0)

                v_ls = []
            
            else:
                v_ls.append(v)

        print('v_ls = %s' % v_ls)
        nd_ls = build_nd_ls(v_ls)      
        nd.children = nd_ls   
        
        return head


    def n_ary_tree_to_str(self, node):
        if node == None:
            return '()'

        s2 = ''
        s1 = '%d, ' % node.val 
        print(s1)
        s2 += s1 

        q = [node] 
        while True:
            if q == []:
                break

            nd = q.pop(0)
            #print(nd.val)
            
            if nd.children != None:
                s1 = str_nd_ls(nd.children)
                s1 = '('+s1[:-2]+'), '
                print(s1)
                s2 += s1
                q += nd.children

        s2 = s2[:-2]
        return s2
