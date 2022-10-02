#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3840/
#
# Implement Disjoint Set with quick union.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/2",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class UnionFind:
    def __init__(self, size):
        self.a = [i for i in range(size)]

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))

    """
        [0, 1, 2, 3, 4, 5, 6]

        union(0, 1)
         v  v
        [0, 1, 2, 3, 4, 5, 6]
        [   0,              ]

        union(1, 2)
            v  v
        [0, 0, 2, 3, 4, 5, 6]
        [      0            ]

        union(1, 3)
            v     v
        [0, 0, 0, 3, 4, 5, 6]
        [         0         ]

        ...
        union(1, 5)
            v           v 
        [0, 0, 0, 0, 4, 4, 4]
         0  1  2  3  4  5  6
        [            0,     ]                   
    """ 
    def union(self, x, y):
        v = get_parent(self.a, x)
        p_idx = get_parent(self.a, y)
        self.a[p_idx] = v

    def connected(self, x, y):
        return get_parent(self.a, x) == get_parent(self.a, y)

def get_parent(a, i):
    idx = i
    while True:
        if a[idx] == idx:
            return idx
        idx = a[idx]
