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
    "date": "2022/9/10",
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

    def init(self, a):
        self.a = a

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))

    """
          [old_r]
     [r]  [x]
      x   y
    """    
    def union(self, x, y):
        old_r = self.a[y]
        r = self.a[x]
        self.a[y] = r
        if old_r != r:
            for i in range(len(self.a)):
                if self.a[i] == old_r:
                    self.a[i] = r

    def connected(self, x, y):
        return self.a[x] == self.a[y]
