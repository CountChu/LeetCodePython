
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    sln.sortColors(nums)
    out = nums
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    test_solution(sln, [2, 0, 1], [0, 1, 2])
    test_solution(sln, [1], [1])
    test_solution(sln, [0], [0])
    test_solution(sln, [0, 0], [0, 0])
    test_solution(sln, [0, 2], [0, 2])
    test_solution(sln, [2, 0], [0, 2])
    test_solution(sln, [1, 0, 1], [0, 1, 1])


