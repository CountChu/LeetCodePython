from data_structure import *
import pdb

def test(sln, module, adjList, answer):
    print('adjList = %s, answer = %s' % (adjList, answer))
    graph = module.ls_to_graph(adjList)
    ls = module.graph_to_ls(graph)
    #pdb.set_trace()
    assert adjList == ls, ls
    #pdb.set_trace()

    out = sln.cloneGraph(graph)
    out_ls = module.graph_to_ls(out)
    #pdb.set_trace()
    assert out_ls == answer, out_ls

def run(sln, module):

	if True:
		test(
			sln,
			module,
			[[2,3],[1],[1]],
			[[2,3],[1],[1]]
			)	
	
	if True:
		test(
			sln,
			module,
			[[2,4],[1,3],[2,4],[1,3]],
			[[2,4],[1,3],[2,4],[1,3]]
			)

	if True:
		test(
			sln,
			module,
			[[]],
			[[]]
			)

	if True:
		test(
			sln,
			module,
			[],
			[]
			)

	if True:
		test(
			sln,
			module,
			[[2], [1]],
			[[2], [1]],
			)

'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    	pass		
'''    	