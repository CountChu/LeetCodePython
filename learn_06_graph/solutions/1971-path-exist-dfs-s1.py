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
    "date": "2022/9/13",
    "design": 0,
    "coding": 0,
    "runtime": "4416 ms",
    "fasterThan": "7%",
    "memory": "106 MB" 
}

#
# It is the official solution.
# https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/4151/
#

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        #br()
        
        stack = [start]
        seen = set()
        
        while stack:
            #print(stack)
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False
