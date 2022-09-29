#
# https://youtu.be/wU6udHRIkcc
#
# Implement Disjoint Set with quick untion in the Abdul Bari way 
# explained in the above YouTube link. 
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
        self.a = [-1] * size
        pass

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))
       
    def find_root(self, x):
        while True:
            if self.a[x] < 0:
                return x
            x = self.a[x]

        return -1

    """
        [      rx  py]
           rx  ry   y    

    """
    def union(self, x, y):
        rx = self.find_root(x)
        ry = self.find_root(y)
        self.a[rx] += self.a[ry]
        self.a[ry] = rx

    def connected(self, x, y):
        return True       
