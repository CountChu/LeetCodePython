from typing import List
import pdb

solution_json = {
    "date": "2021/5/3",
    "design": 6,
    "coding": 8,
    "runtime": "200 ms",
    "memory": "91.7 MB"
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	d = False

    	def build(v, p, r):
    		i = v.index(r)
    		left = v[:i]
    		right = v[i+1:]

    		left_p = p[:i]
    		right_p = p[i:]
    		if d:
    			print(left, r, right, left_p, right_p)

    		root = TreeNode(r)

    		if len(left) == 1:
    			root.left = TreeNode(left[0])
    		elif len(left) >= 2:
    			left_r = left_p.pop(0)
    			root.left = build(left, left_p, left_r)

    		if len(right) == 1:
    			root.right = TreeNode(right[0])
    		elif len(right) >= 2:
    			right_r = right_p.pop(0)
    			root.right = build(right, right_p, right_r)

    		return root

    	p = preorder.copy()
    	r = p.pop(0)
    	root = build(inorder, p, r)

    	#pdb.set_trace()
    	return root