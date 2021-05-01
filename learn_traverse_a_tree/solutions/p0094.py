from typing import List
import pdb

#
# 4 min, 12 min, 44 ms, 15.9 MB
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    	d = False
    	out = []

    	def travel(node):
    		if node == None:
    			return

    		travel(node.left)
    		if d:
    			print(node.val)
    		if node.val != None:	
    			out.append(node.val)
    		travel(node.right)

    	travel(root)	

    	return out



