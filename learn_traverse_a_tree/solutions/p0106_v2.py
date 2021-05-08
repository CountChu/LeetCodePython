from typing import List
import pdb

#
# 2021/5/3: 7 min, 13 min, 212 ms, 92 MB
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    	d = False

    	def build(v, p, r):
    		i = v.index(r)
    		left = v[:i]
    		right = v[i+1:]
    		left_p = p[:i]
    		right_p = p[i:]
    		if d:
    			print(left, r, right, left_p, right_p)
    		assert len(left) == len(left_p)
    		assert len(right) == len(right_p)

    		root = TreeNode(r)
    		if len(left) >= 1:
    			left_r = left_p[-1]
    			if len(left) == 1:
    				root.left = TreeNode(left_r)
    			else:
    				left_p = left_p[:-1]
    				root.left = build(left, left_p, left_r)

    		if len(right) >= 1:
    			right_r = right_p[-1]
    			if len(right) == 1:
    				root.right = TreeNode(right_r)
    			else:
    				right_p = right_p[:-1]
    				root.right = build(right, right_p, right_r)

    		#pdb.set_trace()
    		return root

    	r = postorder[-1]
    	p = postorder[:-1].copy()
    	root = build(inorder, p, r)

    	#pdb.set_trace()
    	return root