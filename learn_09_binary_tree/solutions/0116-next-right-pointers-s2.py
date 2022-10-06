#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition:
#
#   struct Node {
#       int val;
#       Node *left;
#       Node *right;
#       Node *next;
#   }
#
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
#
# Example 1:
#       Input: [1,2,3,4,5,6,7]
#       Output: [1,#,2,3,#,4,5,6,7,#]
#
# Example 2: 
#       Input: []
#       Output: []
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "137 ms",
    "fasterThan": "27%",
    "memory": "15.9 MB" 
}

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
        1
     2      3
   4   5  6   7

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def connect(self, root: Node) -> Node: 
        if root == None:
            return None

        level = 0
        queue = [(level, root)]
        h = {}                          # h[level] = nd_ls
        while True:
            if queue == []:
                break

            #dump_queue(queue)
            level, nd = queue.pop(0)
            #print(level, nd.val)

            if level not in h:
                h[level] = [] 

            h[level].append(nd)

            if nd.left != None:
                queue.append((level + 1, nd.left))
            if nd.right != None:
                queue.append((level + 1, nd.right))
        
        for level, nd_ls in h.items():
            connect(nd_ls)

        return root

def dump_queue(queue):
    ls = []
    for level, nd in queue:
        ls.append((level, nd.val))
    print(ls)

def dump_nd_ls(nd_ls):
    ls = []
    for nd in nd_ls:
        ls.append(nd.val)
    print(ls)

def connect(nd_ls):
    nd0 = nd_ls[0]
    for i in range(1, len(nd_ls)):
        nd1 = nd_ls[i]
        nd0.next = nd1
        nd0 = nd1


