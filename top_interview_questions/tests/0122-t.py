
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, prices, target):
    print("prices = %s, target = %s" % (prices, target))
    out = sln.maxProfit(prices)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [7, 1, 5, 3, 6, 4], 7)
    test_solution(sln, [1, 2, 3, 4, 5], 4)
    test_solution(sln, [7, 6, 4, 3, 1], 0)
    test_solution(sln, [2, 2, 5, 5], 3)
    test_solution(sln, [2, 2, 5], 3)
    test_solution(sln, [5, 7, 2, 7, 3, 3, 5, 3, 0], 9)
    test_solution(sln, [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0], 20)


