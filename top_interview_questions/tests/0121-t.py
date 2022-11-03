
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
    test_solution(sln, [7, 1, 5, 3, 6, 4], 5)
    test_solution(sln, [7, 6, 4, 3, 1], 0)

