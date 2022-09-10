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

"""
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(1, 2)

    [0, 1, 1, 3, 4, 5, 6, 7, 8, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(2, 5)

    [0, 1, 1, 3, 4, 1, 6, 7, 8, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(5, 6)

    [0, 1, 1, 3, 4, 1, 1, 7, 8, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(6, 7)

    [0, 1, 1, 3, 4, 1, 1, 1, 8, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(3, 8)

    [0, 1, 1, 3, 4, 1, 1, 1, 3, 9]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    union(8, 9)

    [0, 1, 1, 3, 4, 1, 1, 1, 3, 3]
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9     

"""

class UnionFind:
    def __init__(self, size):
        self.a = [i for i in range(size)]

    def init(self, a):
        self.a = a 

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))

    def union(self, x, y):
        r = self.a[x]
        #br()
        #self.a[y] = r
        for i in range(len(self.a)): 
            if self.a[i] == self.a[y] or self.a[i] == y:
                self.a[i] = r

    def connected(self, x, y):
        return self.a[x] == self.a[y]
