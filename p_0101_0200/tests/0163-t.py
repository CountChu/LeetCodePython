
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, lower, upper, target):
    print("nums = %s, lower = %d, upper = %d, target = %s" % (nums, lower, upper, target))
    out = sln.findMissingRanges(nums, lower, upper)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]])
    test_solution(sln, [-1], -1, -1, [])
    test_solution(sln, [], 1, 1, [[1, 1]])
