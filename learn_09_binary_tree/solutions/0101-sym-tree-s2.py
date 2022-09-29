from typing import List
import pdb

solution_json = {
    "date": "2021/5/1",
    "design": 4,
    "coding": 8,
    "runtime": "56 ms",
    "memory": "15.8 MB"
}

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	d = False

    	ls1 = []
    	def go1(node, i):
    		if node == None:
    			return

    		go1(node.left, i*2 + 1)	

    		if d:
    			print(node.val)

    		ls1.append((node.val, i))

    		go1(node.right, i*2 + 2)

    	ls2 = []
    	def go2(node, i):
    		if node == None:
    			return

    		go2(node.right, i*2 + 1)	

    		if d:
    			print(node.val)

    		ls2.append((node.val, i))

    		go2(node.left, i*2 + 2)

    	go1(root.left, 0)
    	go2(root.right, 0)

    	#pdb.set_trace()
    	return ls1 == ls2

