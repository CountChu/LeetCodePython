from typing import List
import pdb

solution_json = {
    "date": "2021/5/1",
    "design": 2,
    "coding": 4,
    "runtime": "32 ms",
    "memory": "14.1 MB"
}

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    	d = False
    	out = []

    	def go(node):
    		if node == None:
    			return

    		go(node.left)
    		go(node.right)
    		if d:
    			print(node.val)
    		if node.val != None:
    			out.append(node.val)

    	go(root)

    	#pdb.set_trace()
    	return out

