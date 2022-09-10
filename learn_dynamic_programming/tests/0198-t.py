
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.rob(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 2, 3, 1], 4)
    test_solution(sln, [2, 7, 9, 3, 1], 12)

