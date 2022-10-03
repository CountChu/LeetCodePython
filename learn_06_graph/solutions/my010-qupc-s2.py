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
    "date": "2022/10/3",
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

    def get_a(self):
        return self.a   

    def find(self, x):
        i = x 
        s = []
        r_i = None 
        while True:
            if self.a[i] == i:
                r_i = i
                break 
            s.append(i)
            i = self.a[i]

        for i in s:
            self.a[i] = r_i

        return r_i

    """
        union(3, 4)
                  x  y
         0  1  2  3  4  5  6  7  8  9         
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                     3

        union(8, 3)
                  y              x
         0  1  2  3  4  5  6  7  8  9             
        [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
                  8

        union(4, 9)
                     x              y
         0  1  2  3  4  5  6  7  8  9   
        [0, 1, 2, 8, 3, 5, 5, 7, 8, 9]
                     8              8

    """
    def union(self, x, y):
        x_r_i = self.find(x)
        y_r_i = self.find(y)
        self.a[y_r_i] = x_r_i

    def connected(self, x, y):
        return self.find(x) == self.find(y)
      
