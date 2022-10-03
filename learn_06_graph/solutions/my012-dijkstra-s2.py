#
# https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3862/
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

    def dijkstra(self, start, edges):
        g = {}
        v_d = {}
        for v0, v1, d in edges:
            if v0 not in g:
                g[v0] = {}
            g[v0][v1] = d 


            v_d[v0] = sys.maxsize 
            v_d[v1] = sys.maxsize 

        unseen = set(v_d.keys())
        v_d[start] = 0

        while True:
            if len(unseen) == 0:
                break 
            v0 = find_min_v(unseen, v_d)
            if v0 in g:
                for v1 in g[v0]:
                    v_d[v1] = min(v_d[v1], v_d[v0] + g[v0][v1])
            unseen.remove(v0)
            
        return v_d

def find_min_v(unseen, v_d):
    min_v = None  
    for v in unseen:
        if min_v == None:
            min_v = v 
        else:
            if v_d[min_v] > v_d[v]:
                min_v = v 
    return min_v 
