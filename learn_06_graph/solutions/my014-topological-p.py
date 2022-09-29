#
# https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3886/
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/19",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def topologicalSort(self, edges):
        g = {}
        v_d = {}                        # v_d[v] = in_degree
        for v0, v1 in edges:
            if v0 not in v_d:
                v_d[v0] = 0 
            
            if v1 not in v_d:
                v_d[v1] = 0

            v_d[v1] += 1
 

            if v0 not in g:
                g[v0] = {}
            g[v0][v1] = None

        q = []

        for v in v_d:
            if v_d[v] == 0:
                q.append(v)

        out = []
        while True:
            if q == []:
                break

            v0 = q.pop(0)
            #print(v0)
            out.append(v0)
            if v0 in g:
                for v1 in g[v0]:
                    v_d[v1] -= 1
                    if v_d[v1] == 0:
                        q.append(v1)

        return out

