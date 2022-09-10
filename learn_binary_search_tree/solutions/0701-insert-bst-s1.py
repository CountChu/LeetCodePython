from typing import List
import pdb

solution_json = {
    "date": "2021/5/4",
    "design": 1,
    "coding": 8,
    "runtime": "132 ms",
    "memory": "18.2 MB"   
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    	d = False
    	if root == None:
    		root = TreeNode(val)
    		return root

    	n = root
    	parent = None
    	while True:
    		if n == None:
    			n = TreeNode(val)
    			if d:
    				print('parent.val = %d' % parent.val)
    			if parent.val > n.val:
    				parent.left = n
    			elif parent.val < n.val:
    				parent.right = n
    			else:
    				assert False
    			break

    		if d:
    			print(n.val)

    		if n.val == val:
    			assert False
    		elif n.val < val:
    			parent = n
    			n = n.right
    		else:
    			parent = n
    			n = n.left

    	#pdb.set_trace()
    	return root