
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    n = int(s, 2)
    out = sln.hammingWeight(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, '00000000000000000000000000001011', 3)
    test_solution(sln, '00000000000000000000000010000000', 1)
    test_solution(sln, '11111111111111111111111111111101', 31)

