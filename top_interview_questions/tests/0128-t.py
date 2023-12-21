
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.longestConsecutive(nums)
    print("out = %s" % out)
    print('')

    assert out == target


def run(sln):
    #test_solution(sln, [100, 4, 200, 1, 3, 2], 4)
    #test_solution(sln, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
    #test_solution(sln, [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7)
    #test_solution(sln, [1, 2, 0, 1], 3)