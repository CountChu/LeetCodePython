
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, points, target):
    print("points = %s, target = %s" % (points, target))
    out = sln.minCostConnectPoints(points)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [[0, 0], [2 ,2], [3, 10], [5, 2], [7, 0]], 20)
    #test_solution(sln, [[3, 12], [-2, 5], [-4, 1]], 18)
    #test_solution(sln, [[0, 0], [1, 1], [1, 0], [-1, 1]], 4)
