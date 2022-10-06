from typing import List
import pdb

solution_json = {
    "date": "2021/5/4",
    "design": 18,
    "coding": 27,
    "runtime": "56 ms",
    "memory": "16.9 MB"
}

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = False

        if root == None:
            return None

        h = 0
        q = [(root, h)]
        pre_n = None
        pre_h = -1 
        while True:
            if q == []:
                break

            n, h = q.pop(0)
            n.next = None

            if d:
                print(n.val, h, pre_h)

            if pre_n != None:
                if pre_h == h:
                    pre_n.next = n
                else:
                    pre_n.next = None
            pre_n = n
            pre_h = h    

            if n.left != None:
                q.append((n.left, h+1))

            if n.right != None:
                q.append((n.right, h+1))

        #pdb.set_trace()
        return root

















