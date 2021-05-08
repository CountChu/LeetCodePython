from typing import List
import pdb

#
# 2021/5/4: 10, 21, 1608 ms, 518.2 MB
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = False

        val_path = {}
        def go(n, path):
            
            if d:
                print(n.val, path)
            
            val_path[n.val] = path

            if n.left != None:
                left_path = path + [n.left.val]
                go(n.left, left_path)

            if n.right != None:
                right_path = path + [n.right.val]
                go(n.right, right_path)

        path = [root.val]       
        go(root, path)

        p_path = val_path[p.val]
        q_path = val_path[q.val]

        if d:
            print(p_path)
            print(q_path)

        n = len(p_path)
        if n > len(q_path):
            n = len(q_path)

        count = 0
        for i in range(n):
            if p_path[i] != q_path[i]:
                break
            count += 1

        if d:
            print('i = %d, count = %d' % (i, count))

        out = TreeNode(p_path[count-1])
        #pdb.set_trace()
        return out
