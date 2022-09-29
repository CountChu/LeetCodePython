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
        self.root = [i for i in range(size)]

    def __str__(self):
        return '%s' % self.root

    def dump(self):
        print(str(self))
        
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)    
