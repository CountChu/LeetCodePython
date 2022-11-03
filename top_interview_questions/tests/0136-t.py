
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.singleNumber(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [2, 2, 1], 1)
    test_solution(sln, [4, 1, 2, 1, 2], 4)
    test_solution(sln, [1], 1)


