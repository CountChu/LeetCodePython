
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %s" % (n, target))
    out = sln.isPowerOfThree(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 27, True)
    test_solution(sln, 0, False)
    test_solution(sln, -1, False)
    test_solution(sln, 1, True)


