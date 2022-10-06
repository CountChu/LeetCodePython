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
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

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

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pass

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pass

