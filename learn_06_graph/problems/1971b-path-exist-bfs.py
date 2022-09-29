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
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        return False
