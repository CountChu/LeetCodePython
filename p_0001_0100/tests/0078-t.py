
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.subsets(nums)
    out.sort()
    print("out = %s" % out)
    print('')

def run(sln):
    if True:
        test_solution(
            sln, 
            [1, 2, 3], 
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

    if True:
        test_solution(
            sln,
            [0],
            [[],[0]])

    if True:
        test_solution(
            sln,
            [1, 2],
            [[], [1], [1, 2], [2]])