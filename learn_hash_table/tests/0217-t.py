
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.containsDuplicate(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 2, 3, 1], True)
    test_solution(sln, [1, 2, 3, 4], False)
    test_solution(sln, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)

