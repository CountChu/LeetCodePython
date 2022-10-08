from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/5",
    "design": 4,
    "coding": 13,
    "runtime": "80 ms",
    "memory": "19.6 MB"     
}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    	d = False

    	path1 = find_path(root, p.val)
    	path2 = find_path(root, q.val)

    	if d:
    		print(path1)
    		print(path2)

    	n = len(path1)
    	if n > len(path2):
    		n = len(path2)

    	j = 0
    	for i in range(n):
    		if path1[i] == path2[j]:
    			j += 1
    		else:
    			break

    	nd = TreeNode(path1[j-1])
    	return nd

def find_path(root, v):
	d = False

	path = []
	n = root
	while True:
		if n == None:
			break

		path.append(n.val)	
		if n.val == v:
			break
		elif n.val < v:
			n = n.right
		else:
			n = n.left

	if d:
		print('path = ', path)

	return path	


