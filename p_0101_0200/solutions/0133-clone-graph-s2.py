#
# https://leetcode.com/problems/clone-graph/
#
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) 
# of its neighbors.
#
#   class Node {
#       public int val;
#       public List<Node> neighbors;
#   }
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, 
# and so on. The graph is represented in the test case using an adjacency list.
# 
# An adjacency list is a collection of unordered lists used to represent 
# a finite graph. Each list describes the set of neighbors of a node 
# in the graph.
# 
# The given node will always be the first node with val = 1. You must return 
# the copy of the given node as a reference to the cloned graph.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/27",
    "design": 0,
    "coding": 0,
    "runtime": "75 ms",
    "fasterThan": "47%",
    "memory": "14.5 MB" 
}

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

'''
        1      2      3      4 
    [[2,4], [1,3], [2,4], [1,3]]
'''        

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        graph, nd = node_to_graph(node)

        h = {}
        out = None 
        for v0 in graph:
            h[v0] = Node(v0)
            if out == None:
                out = h[v0]            

        #br()

        stack = [nd]

        seen = set()
        seen.add(nd)

        while True:
            if stack == []:
                break

            nd = stack.pop()
            #print(nd)
            node = h[nd]

            for sub_nd in graph[nd]:
                if sub_nd not in seen:
                    stack.append(sub_nd)
                    seen.add(sub_nd)
                sub_node = h[sub_nd]
                node.neighbors.append(sub_node)

        return out

def dump(stack):
    s = '['
    for nd in stack:
        s += '%d, ' % nd.val 
    s += ']'
    print(s)

def node_to_graph(node):

    stack = []
    stack = [node]

    seen = set()
    seen.add(node.val)
    
    graph = {}

    while True:
        #dump(stack)
        if stack == []:
            break

        nd = stack.pop()
        graph[nd.val] = {}

        #print('seen = %s' % seen)
        for sub_nd in nd.neighbors:
            if sub_nd.val not in seen:
                stack.append(sub_nd)
                seen.add(sub_nd.val)
            graph[nd.val][sub_nd.val] = 1    

    return graph, node.val
