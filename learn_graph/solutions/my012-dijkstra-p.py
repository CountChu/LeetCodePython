#
# https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3862/
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/17",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

def get_min_v(unseen, v_d):
    min_d = sys.maxsize
    min_v = -1
    for v in unseen:
        d = v_d[v]
        if min_d >= d:
            min_d = d 
            min_v = v 
    return min_v 


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def dijkstra(self, start, edges):
        

        graph = {}

        v_d = {}
        for e in edges:
            v0, v1, d = e 
            if v0 not in graph:
                graph[v0] = {}
            graph[v0][v1] = d

            if v0 not in v_d:
                v_d[v0] = sys.maxsize 

            if v1 not in v_d:
                v_d[v1] = sys.maxsize

        v0 = start
        seen = []
        unseen = list(v_d.keys())

        v_d[v0] = 0

        while True:
            #print('--------')
            #print('v0 = %d' % v0)
            if len(graph) == 0:
                break

            for v1, d in graph[v0].items():
                #print(v0, v1, d)
                if v_d[v1] > v_d[v0] + d:
                    v_d[v1] =  v_d[v0] + d
            #print('v_d = %s' % v_d)

            seen.append(v0)
            #print('seen = %s' % seen)

            unseen.remove(v0)
            #print('unseen = %s' % unseen)

            del graph[v0]

            v0 = get_min_v(unseen, v_d)

        return v_d
