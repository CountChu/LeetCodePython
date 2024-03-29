from typing import List
import pdb

solution_json = {
    "date": "2021/5/3",
    "design": 13,
    "coding": 21,
    "runtime": "84 ms",
    "memory": "17.4 MB"
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

        level = {}      # level[i] = count
        i = 1
        level[i] = 1
        q = [root]
        count = 0
        pre_n = None
        while True:
            if q == []:
                break

            if d:
                print(dump_q(q))

            n = q.pop(0)

            if pre_n != None:
                pre_n.next = n
            pre_n = n

            count += 1
            if count == level[i]:               
                if d:
                    print(' '*8, 'end: %d' % n.val)
                i += 1
                level[i] = 2**(i-1) + level[i-1]
                n.next = None
                pre_n = None
                #pdb.set_trace()
            
            if d:
                print(' '*8, n.val, count, level)

            if n.left != None:
                q.append(n.left)

            if n.right != None:
                q.append(n.right)

        #pdb.set_trace()
        return root

def dump_q(q):
    s = '['
    for n in q:
        s += '%d, ' % n.val
    s += ']'
    return s

