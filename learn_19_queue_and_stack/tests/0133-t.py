from data_structure import *
import pdb
br = pdb.set_trace

def test(sln, adjList, answer):
    print('adjList = %s, answer = %s' % (adjList, answer))
    graph = ls_to_graph(adjList)
    ls = graph_to_ls(graph)
    assert adjList == ls, ls

    out = sln.cloneGraph(graph)
    out_ls = graph_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
	
	if True:
		test(
			sln,
			[[2,4], [1,3], [2,4], [1,3]],
			[[2,4], [1,3], [2,4], [1,3]]
			)

	if True:
		test(
			sln,
			[[2,3], [1], [1]],
			[[2,3], [1], [1]]
			)

	if True:
		test(
			sln,
			[[]],
			[[]]
			)

	if True:
		test(
			sln,
			[],
			[]
			)

	if True:
		test(
			sln,
			[[2], [1]],
			[[2], [1]],
			)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def ls_to_graph(ls):
    d = True

    h = {}    # h[v] = nd
    n = len(ls)
    first_nd = None
    for i in range(n):
        v0 = i + 1
        nd_ls = []
        for v in ls[i]:
            if v not in h:
                nd = Node(v)
                h[v] = nd
            nd = h[v]
            nd_ls.append(nd)


        if v0 not in h:
            nd0 = Node(v0)
            h[v0] = nd0
        nd0 = h[v0]
        nd0.neighbors = nd_ls

        if first_nd == None:
            first_nd = nd0

    return first_nd

def graph_to_ls(node):
    d = False 

    if node == None:
        return []
    
    table = [] # (val, val_ls)    
    h = {}  # h[nd.val] = val_ls  (visited neighbors)
    stack = [node]
    while True:
        if d:
            dump_stack(stack)

        if stack == []:
            break

        top = stack[-1]
        if d:
            print('top: %d' % top.val)

        if top.val not in h:
            h[top.val] = []

        for nd in top.neighbors:
            if nd.val not in h:
                stack.append(nd)
                break
            else:
                if nd.val not in h[top.val]:
                    h[top.val].append(nd.val)                         

        if d:
            print('h = %s' % h)

        if len(h[top.val]) == len(top.neighbors):
            nd = stack.pop()
            val_ls = [nd.val for nd in top.neighbors]             
            if d:
                print('nd: %d, %s' % (nd.val, val_ls))
            table.append((nd.val, val_ls))
            continue

    table.sort(key = lambda x: x[0])
    out = [row[1] for row in table]
    return out

def dump_stack(stack):
    s = 'stack: '
    for nd in stack:
        s += '%d, ' % nd.val
    print(s)


