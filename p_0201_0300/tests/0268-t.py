
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.missingNumber(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [3, 0, 1], 2)
    test_solution(sln, [0, 1], 2)
    test_solution(sln, [9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
    test_solution(sln, [1], 0)

