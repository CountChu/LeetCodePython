
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, gas, cost, target):
    print("gas = %s, cost = %s, target = %s" % (gas, cost, target))
    out = sln.canCompleteCircuit(gas, cost)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
    #test_solution(sln, [2, 3, 4], [3, 4, 3], -1)
    #test_solution(sln, [4, 5, 3, 1, 4], [5, 4, 3, 4, 2], -1)
    #test_solution(sln, [0, 0, 0, 0, 2], [0, 0, 0, 1, 0], 4)



