
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %s" % (n, target))
    out = sln.isHappy(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 19, True)
    test_solution(sln, 2, False)
