#
# https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3886/
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

    def topologicalSort(self, edges):
        g = {}
        v_in = {}
        for v0, v1 in edges:
            if v0 not in g:
                g[v0] = {} 
            g[v0][v1] = 1
            v_in[v0] = 0
            v_in[v1] = 0

        for v0 in g:
            for v1 in g[v0]:
                v_in[v1] += 1 

        out = []
        while True:
            if len(v_in) == 0:
                break

            min_v = find_min_v(v_in)
            print(min_v)
            out.append(min_v)

            if min_v in g:
                for v1 in g[min_v]:
                    v_in[v1] -= 1

            del v_in[min_v]

        return out

def find_min_v(v_in):
    min_v = None 
    for v in v_in:
        if min_v == None:
            min_v = v
        else:
            if v_in[v] < v_in[min_v]:
                min_v = v 
    assert min_v != None 
    
    return min_v 