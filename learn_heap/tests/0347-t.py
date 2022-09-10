
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, k, target):
    print("nums = %s, k = %d, target = %s" % (nums, k, target))
    out = sln.topKFrequent(nums, k)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 1, 1, 2, 2, 3], 2, [1, 2])
    test_solution(sln, [1], 1, [1])
    test_solution(sln, [3, 0, 1, 0], 1, [0])
    test_solution(sln, [4, 1, -1, 2, -1, 2, 3], 2, [-1, 2])