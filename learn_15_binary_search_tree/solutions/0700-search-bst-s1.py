from typing import List
import pdb

solution_json = {
    "date": "2021/5/4",
    "design": 2,
    "coding": 4,
    "runtime": "80 ms",
    "memory": "17.4 MB"
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    	d = False

    	found = None
    	n = root
    	while True:
    		if n == None:
    			break

    		if d:
    			print(n.val)

    		if n.val == val:
    			found = n
    			break

    		elif n.val > val:
    			n = n.left

    		else:
    			n = n.right

    	return found
    


