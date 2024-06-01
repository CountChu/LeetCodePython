
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %s" % (n, target))
    out = sln.countAndSay(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 1, "1")
    test_solution(sln, 4, "1211")

