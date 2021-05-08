from typing import List
import pdb

#
# 2021/5/2: 3 mins, 14 mins, 68 ms, 17.5 MB
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    	d = False

    	if root == None:
    		return False

    	h = {}   # h[node] == sum
    	def go(node, ctx):
    		if d:
    			print(node.val)

    		if ctx['out']:
    			return

    		if node.left != None:
    			h[node.left] =h[node] + node.left.val
    			go(node.left, ctx)

    		if node.right != None:
    			h[node.right] = h[node] + node.right.val
    			go(node.right, ctx)

    		if node.left == None and node.right == None:
    			if h[node] == targetSum:
    				ctx['out'] = True	

    	ctx = {'out': False}
    	h[root] = root.val
    	go(root, ctx)
    	
    	return ctx['out']