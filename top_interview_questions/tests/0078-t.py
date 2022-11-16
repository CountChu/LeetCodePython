
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.subsets(nums)
    print("out = %s" % out)
    print('')

    assert out == target


def run(sln):
    if 1 == 1:
        test_solution(
            sln, 
            [1, 2, 3], 
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    if 1 == 1:
        test_solution(
            sln,
            [0],
            [[],[0]])
