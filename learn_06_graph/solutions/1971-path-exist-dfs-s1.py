#
# https://leetcode.com/problems/find-if-path-exists-in-graph/
#
# Given an array...
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
    "date": "2022/9/13",
    "design": 0,
    "coding": 0,
    "runtime": "4653 ms",
    "fasterThan": "5%",
    "memory": "106.3 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def validPath(self, n: int, edges: List[List[int]], s: int, d: int) -> bool:
        g = [[] for _ in range(n)]
        for v0, v1 in edges:
            g[v0].append(v1)
            g[v1].append(v0)
        
        stack =[s]
        seen = set() 

        while True:
            if stack == []:
                break

            v = stack.pop()

            if v == d:
                return True

            if v in seen:
                continue 

            seen.add(v)

            for w in g[v]:
                stack.append(w)

        return False
