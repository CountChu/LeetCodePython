from typing import List
import pdb

solution_json = {
    "date": "2021/5/1",
    "design": 6,
    "coding": 8,
    "runtime": "57 ms",
    "fasterThan": "57%",    
    "memory": "14.2 MB"
}

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d = False
        
        if root == None:
            return []

        out = []

        node = root
        q = [(node, 0)]
        hash = {} 
        while True:
            if q == []:
                break

            node, level = q.pop(0)
            if d:
                print(node.val, level)

            if level not in hash:
                hash[level] = []
            hash[level].append(node.val)

            if node.left != None:
                if node.left.val != None:
                    q.append((node.left, level+1))
            if node.right != None:
                if node.right.val != None:
                    q.append((node.right, level+1))

        for v in hash.values():
            out.append(v)
        
        return out

