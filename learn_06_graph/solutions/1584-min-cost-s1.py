#
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#
# You are given an array points representing integer coordinates of some points 
# on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute 
# value of val.
#
# Return the minimum cost to make all points connected. All points are connected 
# if there is exactly one simple path between any two points.
#
# Example 1:
#       Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#       Output: 20
#
# Example 2: 
#       Input: points = [[3,12],[-2,5],[-4,1]]
#       Output: 18
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/15",
    "design": 0,
    "coding": 0,
    "runtime": "7284 ms",
    "fasterThan": "8%",
    "memory": "108.3 MB" 
}


def get_m_dist(p0, p1):
    x0, y0 = p0
    x1, y1 = p1 
    return abs(x0-x1) + abs(y0-y1)

def root(a, x):
    while True:
        px = a[x]
        if px == x: 
            return px
        x = px

"""
    [x]
     y
"""
def union(a, x, y):
    rx = root(a, x)
    ry = root(a, y)
    a[ry] = rx

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v_num = len(points)
        g = {}
        for i in range(v_num - 1):
            if i not in g:
                g[i] = {}
            for j in range(i+1, v_num):
                g[i][j] = get_m_dist(points[i], points[j])
                #g[i][j] = 0

        e_ls = []
        for i in g:
            for j in g[i]:
                e_ls.append((i, j, g[i][j]))
                #print(i, j, g[i][j])
        e_ls.sort(key=lambda x: x[2])

        out = 0
        a = [i for i in range(v_num)]
        for e in e_ls:
            x, y, d = e  
            if root(a, x) != root(a, y):
                union(a, x, y)
                out += d

        return out

    
