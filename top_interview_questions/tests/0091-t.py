
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.numDecodings(s)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, "12", 2)
    test_solution(sln, "226", 3)
    test_solution(sln, "2126", 5)
    test_solution(sln, "06", 0)
    test_solution(sln, "10", 1)
    test_solution(sln, "111111111111111111111111111111111111111111111", 1836311903)
    test_solution(sln, "27", 1)
    test_solution(sln, '0', 0)
    test_solution(sln, '2101', 1)
    test_solution(sln, '1201234', 3)
    test_solution(sln, '123123', 9)
