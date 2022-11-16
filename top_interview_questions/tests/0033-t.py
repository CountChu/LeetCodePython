
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target, target2):
    print("nums = %s, target = %d, target2 = %d" % (nums, target, target2))
    out = sln.search(nums, target)
    print("out = %s" % out)
    print('')

    assert out == target2

def run(sln):
    test_solution(sln, [5, 6, 7, 0, 1, 2, 3, 4], 0, 3)
    test_solution(sln, [4, 5, 6, 7, 0, 1, 2], 0, 4)
    test_solution(sln, [4, 5, 6, 7, 0, 1, 2], 3, -1)
    test_solution(sln, [1], 0, -1)
    test_solution(sln, [1, 3], 0, -1)
    test_solution(sln, [3, 5, 1], 3, 0)
    test_solution(sln, [1, 3], 3, 1)
    test_solution(sln, [4, 5, 6, 7, 0, 1, 2], 2, 6)
    test_solution(sln, [6, 7, 1, 2, 3, 4, 5], 6, 0)
    test_solution(sln, [4, 5, 6, 7, 8, 1, 2, 3], 8, 4)
