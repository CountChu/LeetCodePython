#
# https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/
#


from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/18",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def bellman(self, start, edges):

        g = {}
        v_d = {}
        for u, v, d in edges:
            if u not in g:
                g[u] = {}
            g[u][v] = d

            if u not in v_d:
                v_d[u] = sys.maxsize 
            if v not in v_d:
                v_d[v] = sys.maxsize  

        v_d[start] = 0 

        while True:
            changed = False
            for u, vd in g.items():
                for v, d in vd.items():
                    if v_d[v] > v_d[u] + g[u][v]:
                        v_d[v] = v_d[u] + g[u][v]
                        changed = True 
                    #print(u, v, d)

            if not changed:
                break

        return v_d