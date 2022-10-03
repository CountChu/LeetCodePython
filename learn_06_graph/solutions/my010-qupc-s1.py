#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
#
# Implement Disjoint Set with quick union and path compression.
#
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/12",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

#
# Here is the official solution.
#        

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def init(self, a):
        self.root = a        

    def __str__(self):
        return '%s' % self.root

    def dump(self):
        print(str(self))

    def get_a(self):
        return self.root        

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
      
