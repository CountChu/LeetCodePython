#
# https://leetcode.com/problems/find-if-path-exists-in-graph/
#
# There is a bi-directional graph with n vertices, where each vertex is labeled 
# from 0 to n - 1 (inclusive).
#
# DFS solution
#
# Example 1:
#       Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
#       Output: true
#
# Example 2: 
#       Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
#       Output: false
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/3",
    "design": 0,
    "coding": 0,
    "runtime": "4193 ms",
    "fasterThan": "25%",
    "memory": "118.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
        (0, 1)
        (0, 2)
        (1, 3)
        (2, 3)
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for v0, v1 in edges:
            if v0 not in g:
                g[v0] = {}
            g[v0][v1] = 1

            if v1 not in g:
                g[v1] = {}
            g[v1][v0] = 1

        stack = [source]
        seen = set()
        while True:
            if stack == []:
                break

            v0 = stack.pop()
            #print(v0)

            if v0 == destination:
                return True
            
            seen.add(v0)

            if v0 not in g:
                continue
            
            v_ls = list(g[v0].keys())
            for v1 in v_ls:
                if v1 not in seen:
                    stack.append(v1)

        return False















