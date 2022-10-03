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
# Please implement it with Prim's algorithm.
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
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = {}
        for i in range(n - 1):
            if i not in g:
                g[i] = {}
            for j in range(i + 1, n):
                g[i][j] = get_dist(points[i], points[j])
                if j not in g:
                    g[j] = {}
                g[j][i] = get_dist(points[i], points[j])

        out = 0
        seen_ls = set()
        seen_ls.add(0)

        while True:
            if len(seen_ls) == n:
                break

            e_ls = get_ordered_edges(g, seen_ls)
            print(e_ls)
            v0, v1, d = e_ls[0]
            out += d

            for v0 in seen_ls:
                del_edge(g, v0, v1)
            
            seen_ls.add(v1)

        return out

def get_dist(p0, p1):
    x0, y0 = p0 
    x1, y1 = p1 
    return abs(x0 - x1) + abs(y0 - y1)

def get_ordered_edges(g, seen_ls):
    e_ls = []
    for v0 in seen_ls:
        for v1 in g[v0]:
            if v1 in seen_ls:
                continue

            d = g[v0][v1]
            e_ls.append((v0, v1, d)) 
    e_ls.sort(key = lambda x: x[2])
    
    return e_ls

def del_edge(g, v0, v1):
    if v0 in g:
        del g[v0][v1]
        if g[v0] == {}:
            del g[v0]

    if v1 in g:
        del g[v1][v0]
        if g[v1] == {}:
            del g[v1]












    
