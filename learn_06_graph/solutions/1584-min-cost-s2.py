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
# Please implement it with Kruskal's algorithm.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/3",
    "design": 0,
    "coding": 0,
    "runtime": "3493 ms",
    "fasterThan": "57%",
    "memory": "107.6 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = {}
        for i in range(0, n - 1):
            if i not in g:
                g[i] = {}
            for j in range(i+1, n):
                #print(i, j)
                g[i][j] = get_distance(points[i], points[j])
                
        e_ls = []
        for i in g:
            for j in g[i]:
                e_ls.append((i, j, g[i][j]))
        
        e_ls.sort(key = lambda x: x[2])

        #br()

        out = 0
        a = [i for i in range(n)]
        count = 0
        for v0, v1, d in e_ls:
            v0_r = find_root(a, v0)
            v1_r = find_root(a, v1)
            if v0_r != v1_r:
                union(a, v0, v1)
                out += d 
                count += 1 
                if count == n - 1:
                    break

        return out

def get_distance(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return abs(x0 - x1) + abs(y0 - y1)

"""
                  i
         0  1  2  3  4
    a = [0, 1, 1, 2, 4]

"""
def find_root(a, i):
    p_i = i
    while True:
        if a[p_i] == p_i:
            return p_i 

        p_i = a[p_i]

"""
            v     x  v  y
         0  1  2  3  4  5
    a = [0, 1, 1, 2, 4, 4]
        [0, 1, 1, 2, 1, 4]
"""
def union(a, x, y):
    x_r_i = find_root(a, x)
    y_r_i = find_root(a, y)
    a[y_r_i] = x_r_i













    
