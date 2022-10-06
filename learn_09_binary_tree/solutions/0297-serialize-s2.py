#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Serialization is the process of converting a data structure or object 
# into a sequence of bits so that it can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed later 
# in the same or another computer environment.
#
# Example 1:
#       Input: root = [1,2,3,null,null,4,5]
#       Output: [1,2,3,null,null,4,5]
#
# Example 2: 
#       Input: root = []
#       Output: []
# 

from typing import List
import sys
import json
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "397 ms",
    "fasterThan": "19%",
    "memory": "20 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

#
# !!! Don't paste the class TreeNode in the LeetCode !!!
#        

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
#

class Codec:

    '''
             1
         2      3 
       N   N  4   5  
    '''
    def serialize(self, root):
        if root == None:
            return '[]'

        nd = root
        queue = [nd]
        out = []
        while True:
            if queue == []:
                break

            nd = queue.pop(0)
            if nd == None:
                out.append(None)
                #print('N')
                continue 
            
            #print(nd.val)
            out.append(nd.val)

            queue.append(nd.left)
            queue.append(nd.right)

        while True:
            if out == []:
                break 

            if out[-1] != None:
                break

            out.pop()

        return json.dumps(out)

    def deserialize(self, data):
        ls = json.loads(data)
        if ls == []:
            return None 

        v = ls.pop(0)
        nd = TreeNode(v)
        queue  = [nd]
        head = nd
        while True:
            nd = queue.pop(0)
            
            if ls == []:
                break
            
            left = ls.pop(0)
            if left == None:
                nd.left = None
            else:
                nd.left = TreeNode(left)
                queue.append(nd.left)

            if ls == []:
                break 

            right = ls.pop(0)
            if right == None:
                nd.right = None
            else:
                nd.right = TreeNode(right)
                queue.append(nd.right)

        return head













