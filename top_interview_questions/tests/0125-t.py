
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.isPalindrome(s)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, "A man, a plan, a canal: Panama", True)
    test_solution(sln, "race a car", False)
    test_solution(sln, " ", True)
    test_solution(sln, "0P", False)
