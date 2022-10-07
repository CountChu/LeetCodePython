from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/4",
    "design": 15,
    "coding": 15,
    "runtime": "80 ms",
    "memory": "22.2 MB"
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.d = False

        self.root = root
        self.s = []
        
        n = self.root
        while True:
            self.s.append((n.val, n))
            if n.left != None:
                n = n.left
            else:
                break

        if self.d:
            print(self.dumpStack())

    def dump(self):
        pass

    def next(self) -> int:
        val, n = self.s.pop()
        if n.right != None:
            n = n.right
            while True:
                self.s.append((n.val, n))
                if n.left != None:
                    n = n.left
                else:
                    break

        if self.d:
            print('next(): val = %d' % val)

        return val        

    def hasNext(self) -> bool:
        return len(self.s) != 0   

    def dumpStack(self):
        str = '['
        for val, n in self.s:
            str += '%d, ' % val
        str += ']'
        return str
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
