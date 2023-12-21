
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.partition(s)
    out.sort()
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, "aab", [["a", "a", "b"], ["aa", "b"]])
    test_solution(sln, "a", [["a"]])
    test_solution(sln, "efe", [["e", "f", "e"], ["efe"]])

