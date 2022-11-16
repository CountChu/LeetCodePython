
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, m, n, target):
    print("m = %d, n = %d, target = %s" % (m, n, target))
    out = sln.uniquePaths(m, n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 3, 7, 28)
    test_solution(sln, 3, 2, 3)
    test_solution(sln, 4, 4, 20)
