from typing import List
import pdb

#
# 2021/5/1: 1 min, 10 mins, 52 ms, 17.9 MB 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    	d = False

    	if root == None:
    		return 0

    	ctx = {'maxLevel': 0}

    	def go(ctx, node, level):
    		#pdb.set_trace()
    		if node == None:
    			return 
    		if node.val == None:
    			return

    		if d:
    			print(node.val, level)
    		if ctx['maxLevel'] < level:
    			ctx['maxLevel'] = level

    		go(ctx, node.left, level+1)
    		go(ctx, node.right, level+1)

    	go(ctx, root, 1)
    	return ctx['maxLevel']