#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3879/
#
# Implement Disjoint Set with weighted quick union.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/11",
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
        self.w = [1] * size 
        self.a = [i for i in range(size)]
        pass

    def dump(self):
        print('w = %s' % self.w)
        print('a = %s' % self.a)

    def get_w(self):
        return self.w 

    def get_a(self):
        return self.a 
       
    def get_root(self, x):
        while True:
            px = self.a[x]
            if px == x:
                return px
            x = px  
        return -1

    """
        [ppx, px, ppy, py] 
          px   x   py   y
    """
    def union(self, x, y):
        rx = self.get_root(x)
        ry = self.get_root(y)
        if self.w[rx] > self.w[ry]:
            self.a[ry] = rx
        elif self.w[rx] < self.w[ry]:
            self.a[rx] = ry
        else:
            self.a[ry] = rx
            self.w[rx] += 1

    def connected(self, x, y):
        return True      



































