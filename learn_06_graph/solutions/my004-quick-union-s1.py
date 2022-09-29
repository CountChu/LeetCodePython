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
        self.a = [i for i in range(size)]

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))


    def find_root(self, x):  
        while True:
            if self.a[x] == x:
                return x 
            x = self.a[x]
        return -1

    """
     [ rx      px  ry      py]
       rx  px   x  ry  py   y 

     [ rx      px  rx      py]
       rx  px   x  ry  py   y 


    """ 
    def union(self, x, y):
        rx = self.find_root(x)
        ry = self.find_root(y)
        self.a[ry] = rx

    def connected(self, x, y):
        rx = self.find_root(x)
        ry = self.find_root(y)
        return rx == ry