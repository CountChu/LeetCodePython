
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target, target2):
    print("nums = %s, target = %d, target2 = %s" % (nums, target, target2))
    out = sln.searchRange(nums, target)
    print("out = %s" % out)
    print('')

    assert out == target2

def run(sln):
    test_solution(sln, [5, 7, 7, 8, 8, 10], 8, [3, 4])
    test_solution(sln, [5, 7, 7, 8, 8, 10], 6, [-1, -1])
    test_solution(sln, [], 0, [-1, -1])

