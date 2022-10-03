#
# https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/
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

    def bellman(self, start, edges):
        g = {}
        v_d = {}
        for v0, v1, w in edges:
            if v0 not in g:
                g[v0] = {}
            g[v0][v1] = w
            v_d[v0] = sys.maxsize 
            v_d[v1] = sys.maxsize 

        v_d[start] = 0
        while True:
            changed = False
            for v0 in g:
                for v1 in g[v0]:
                    w = g[v0][v1]
                    #print(v0, v1, w)
                    if v_d[v1] > v_d[v0] + w:
                        v_d[v1] = v_d[v0] + w 
                        changed = True
            if not changed:
                break 
        return v_d