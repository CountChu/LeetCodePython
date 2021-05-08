from typing import List
import pdb

#
# 2021/5/4: 18 mins, 27 mins, 56 ms, 16.9 MB
#

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

    def tree_to_ls(self, root):
        d = False

        if root == None:
            return []

        out_ls = []

        #pdb.set_trace()
        q = [root]
        while True:
            if q == []:
                break

            n = q.pop(0)
            if d:
                print(n.val)

            out_ls.append(n.val)
            if n.next == None:
                out_ls.append('#')

            if n.left != None:
                q.append(n.left)

            if n.right != None:
                q.append(n.right)

        #pdb.set_trace()
        return out_ls















