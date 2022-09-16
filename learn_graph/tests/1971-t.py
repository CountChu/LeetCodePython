
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, edges, source, destination, target):
    print("n = %d, edges = %s, source = %d, destination = %d, target = %s" % (
        n, edges, source, destination, target))
    out = sln.validPath(n, edges, source, destination)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 3, [[0,1],[1,2],[2,0]], 0, 2, True)
    test_solution(sln, 6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False)
