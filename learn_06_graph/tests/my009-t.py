
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, x, target):
    print("nums = %s, x = %d, target = %s" % (nums, x, target))
    sln.compress_path(nums, x)
    out = nums
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [0, 0, 1, 2, 3, 4], 5, [0, 0, 0, 0, 0, 0])