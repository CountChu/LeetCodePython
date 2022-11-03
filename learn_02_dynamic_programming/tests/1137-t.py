
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %d" % (n, target))
    out = sln.tribonacci(n)
    print("out = %s" % out)
    print('')

    assert out == target


def run(sln):
    test_solution(sln, 1, 1)
    test_solution(sln, 4, 4)
    test_solution(sln, 25, 1389537)
    test_solution(sln, 3, 2)

