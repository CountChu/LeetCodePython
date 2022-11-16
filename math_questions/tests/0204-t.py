
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %d" % (n, target))
    out = sln.countPrimes(n)
    print("out = %d" % out)
    print('')

    assert out == target


def run(sln):
    test_solution(sln, 10, 4)
    test_solution(sln, 0, 0)
    test_solution(sln, 1, 0)
    test_solution(sln, 2, 0)
    test_solution(sln, 1000, 168)
    test_solution(sln, 136649, 12727)
