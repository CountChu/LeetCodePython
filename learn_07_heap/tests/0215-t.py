
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, k, target):
    print("nums = %s, k = %d, target = %s" % (nums, k, target))
    out = sln.findKthLargest(nums, k)
    print("out = %d" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [3,2,1,5,6,4], 2, 5)
    test_solution(sln, [3,2,3,1,2,4,5,5,6], 4, 4)
