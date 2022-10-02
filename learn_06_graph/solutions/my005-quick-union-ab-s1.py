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
        self.a = [-1] * size
        pass

    def __str__(self):
        return '%s' % self.a

    def dump(self):
        print(str(self))
       
    """ 
          0   1   2   3   4   5   6   7   8
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]

        union(1, 2)
              v   v
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        [    -2   1                        ] 

        ...
        union(2, 4)
                 v      v
        [-1, -2, 1, -2, 3, -2, 5, -2, 7]
        [    -4   ,  1                 ]

    """  
    def union(self, x, y):
        x_r_i = find_root(self.a, x)
        y_r_i = find_root(self.a, y)
        self.a[x_r_i] += self.a[y_r_i]
        self.a[y_r_i] = x_r_i

    def connected(self, x, y):
        x_r_i = find_root(self.a, x)
        y_r_i = find_root(self.a, y)
        return self.a[x_r_i] == self.a[y_r_i]

def find_root(a, i):
    p_i = i
    while True:
        if a[p_i] <= -1:
            return p_i
        p_i = a[p_i]

    return -1
