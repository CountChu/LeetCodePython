from typing import List
import pdb

solution_json = {
    "date": "2021/5/4",
    "design": 1,
    "coding": 7,
    "runtime": "48 ms",
    "memory": "18.5 MB"
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    	d = False

    	if root == None:
    		return True

    	last_v = None
    	ctx = {'last_v': None, 'stop': False}

    	def go(n, ctx):
    		if ctx['stop']:
    			return

    		if n.left != None:
    			go(n.left, ctx)

    		if d:
    			print(n.val, ctx['last_v'])

    		if ctx['last_v'] != None:
    			if ctx['last_v'] >= n.val:
    				ctx['stop'] = True

    		ctx['last_v'] = n.val

    		if n.right != None:
    			go(n.right, ctx)

    	go(root, ctx)

    	#pdb.set_trace()
    	return not ctx['stop']
