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
    "again": ["2022/10/2"],
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
    

    """
        union(4, 3)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                  y  x
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                  4  4

        union(3, 8)
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
                  x              y
        [0, 1, 2, 4, 4, 5, 6, 7, 8, 9]
                                 4

    """
    def union(self, x, y):
        x_r_i = find_root(self.a, x)
        y_r_i = find_root(self.a, y)
        if self.w[x_r_i] == self.w[y_r_i]:
            self.a[y_r_i] = x_r_i
            self.w[x_r_i] += 1
        elif self.w[x_r_i] > self.w[y_r_i]:
            self.a[y_r_i] = x_r_i
        else:
            self.a[x_r_i] = y_r_i

    def connected(self, x, y):
        x_r_i = find_root(self.a, x)
        y_r_i = find_root(self.a, y)        
        return self.a[x_r_i] == self.a[y_r_i]

def find_root(a, i):
    p_i = i
    while True:
        if a[p_i] == p_i:
            return p_i 
        p_i = a[p_i]



































