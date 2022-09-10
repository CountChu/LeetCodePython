
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, cost, target):
    print("cost = %s, target = %d" % (cost, target))
    out = sln.minCostClimbingStairs(cost)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [10,15,20], 15)
    test_solution(sln, [1, 100], 1)    
    test_solution(sln, [1, 100, 1], 2)
    test_solution(sln, [1, 100, 1, 1], 2)
    test_solution(sln, [1, 100, 1, 1, 1], 3)
    test_solution(sln, [1, 100, 1, 1, 1, 100], 3)
    test_solution(sln, [1, 100, 1, 1, 1, 100, 1], 4)
    test_solution(sln, [1, 100, 1, 1, 1, 100, 1, 1], 4)
    test_solution(sln, [1, 100, 1, 1, 1, 100, 1, 1, 100], 5)
    test_solution(sln, [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
