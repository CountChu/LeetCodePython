from typing import List
import pdb

solution_json = {
    "date": "2021/5/5",
    "design": 30,
    "coding": 60,
    "runtime": "208 ms",
    "memory": "21.3 MB"
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        d = False
        v = nums
        n = len(v)
        self.root = None
        self.k = k
        nd = None
        self.count = 0
        for i in range(n):            
            if self.root == None:
                self.root = TreeNode(v[i])
            else:
                insert(self.root, v[i])

            self.count += 1
            if d:
                print(v[i], self.count)            

            if self.count == self.k + 1:
                self.root = delete(self.root)
                self.count -= 1

        #pdb.set_trace()

    def add(self, val: int) -> int:
        d = False

        if d:
            print('add() val = ', val)

        if self.root == None:
            self.root = TreeNode(val)
            self.count += 1
            klargest = self.root.val
            return klargest

        insert(self.root, val)
        self.count += 1

        if self.count == self.k + 1:
            self.root = delete(self.root)
            self.count -= 1

        leftmost, _ = get_leftmost(self.root)
        klargest = leftmost.val

        if d:
            print('add() klargest = ', klargest)

        return klargest

def insert(root, v):
    d = False
    nd = root

    while True:
        if d:
            print(nd.val)

        if nd.val < v:
            if nd.right != None:
                nd = nd.right
            else:
                nd.right = TreeNode(v)
                break
        else:
            if nd.left != None:
                nd = nd.left
            else:
                nd.left = TreeNode(v)
                break

def dump_node(nd):
    nd_str = 'None'
    if nd != None:
        nd_str = str(nd.val)
    return nd_str

def delete(root):
    d = False

    leftmost, parent = get_leftmost(root)

    if d:
        print('delete() root:', dump_node(root), 'leftmost: ', dump_node(leftmost), 'parent: ', dump_node(parent))

    if parent != None:
        parent.left = leftmost.right
    else:
        root = leftmost.right

    return root

def get_leftmost(root):
    d = False

    parent = None
    leftmost = None
    nd = root
    while True:
        if nd == None:
            leftmost = parent
            parent = None

        if nd.left != None:
            parent = nd
            nd = nd.left
        else:
            leftmost = nd
            break

    return leftmost, parent        





class Solution:
    def func(self, nums):
        pdb.set_trace()
