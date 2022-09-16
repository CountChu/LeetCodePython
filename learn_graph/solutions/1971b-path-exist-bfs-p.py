#
# https://leetcode.com/problems/find-if-path-exists-in-graph/
#
# BFS solution
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
    "date": "2022/9/14",
    "design": 0,
    "coding": 0,
    "runtime": "3829 ms",
    "fasterThan": "22%",
    "memory": "103 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for v0, v1 in edges:
            g[v0].append(v1)
            g[v1].append(v0)
        
        q = []
        seen = set()

        q.append(source)
        
        while True:
            v0 = q.pop(0)
            if v0 == destination:
                return True
            
            seen.add(v0)

            for v1 in g[v0]:
                if v1 not in seen:
                    q.append(v1)

            if q == []:
                break 

        return False
