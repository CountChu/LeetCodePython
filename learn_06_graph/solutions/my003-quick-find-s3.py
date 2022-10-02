#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3878/
#
# Implement Disjoint Set with quick find.
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
        pass

    def init(self, a):
        self.a = a

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))
        
    """
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = a

        union(3, 4)
                  v  v
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [         3, 3,              ]

        union(8, 3)
                  v              v
        [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
        [         8, 8           8          

    """
    def union(self, x, y):
        old_v = self.a[y]
        for i in range(len(self.a)):
            if self.a[i] == old_v:
                self.a[i] = self.a[x]

    def connected(self, x, y):
        return self.a[x] == self.a[y]
