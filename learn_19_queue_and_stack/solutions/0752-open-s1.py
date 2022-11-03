from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/15",
    "design": 11,
    "coding": 45,
    "runtime": "2568 ms",
    "memory": "18 MB"
}  

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def openLock(self, deadends: List[str], target: str) -> int:
        d = False

        #
        # Transform deadends into dead_ls
        #

        dead_ls = []
        for deadend in deadends:
            dead = []
            for i in range(len(deadend)):
                c = deadend[i]
                dead.append(int(c))
            dead_ls.append(tuple(dead))

        if d:
            print('dead_ls = %s' % dead_ls)

        #
        # Transform target into target_nd
        #

        target_nd = []
        for i in range(len(target)):
            c = target[i]
            target_nd.append(int(c))
        target_nd = tuple(target_nd)

        if d:
            print('target_nd = ', target_nd)

        #
        # Core task.
        #

        nd = (0, 0, 0, 0)
        level = 0

        q = [(nd, level)] # queue

        v = {}  # visisted, v[nd] = level
        out = -1
        while True:
            if q == []:
                break

            nd, level = q.pop(0)
            if d:
                print(nd)

            if nd in v:                
                continue

            if nd in dead_ls:
                continue

            v[nd] = level

            if nd == target_nd:
                out = level
                break
        
            nd_ls = []

            nd_ls.append((rotate(nd, 0, +1), level+1))
            nd_ls.append((rotate(nd, 1, +1), level+1))
            nd_ls.append((rotate(nd, 2, +1), level+1))
            nd_ls.append((rotate(nd, 3, +1), level+1))
            nd_ls.append((rotate(nd, 0, -1), level+1))
            nd_ls.append((rotate(nd, 1, -1), level+1))
            nd_ls.append((rotate(nd, 2, -1), level+1))
            nd_ls.append((rotate(nd, 3, -1), level+1))

            q += nd_ls

        if d:
            for nd, level in v.items():
                print(nd, level)
        
        #pdb.set_trace()
        return out


def rotate(nd, idx, d):
    next_nd = list(nd)

    next_nd[idx] += d

    if next_nd[idx] == 10:
        next_nd[idx] = 0
    
    if next_nd[idx] == -1:
        next_nd[idx] = 9

    return tuple(next_nd)

