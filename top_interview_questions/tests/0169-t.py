
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.majorityElement(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    #test_solution(sln, [3, 2, 3], 3)
    test_solution(sln, [2, 2, 1, 1, 1, 2, 2], 2)
