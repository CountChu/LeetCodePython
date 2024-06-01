
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.firstUniqChar(s)
    print("out = %d" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 'leetcode', 0)
    test_solution(sln, 'loveleetcode', 2)
    test_solution(sln, 'aabb', -1)

