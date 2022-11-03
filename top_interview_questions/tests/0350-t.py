
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums1, nums2, target):
    print("nums1 = %s, nums2 = %s, target = %s" % (nums1, nums2, target))
    out = sln.intersect(nums1, nums2)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 2, 2, 1], [2, 2], [2, 2])
    test_solution(sln, [4, 9, 5], [9, 4, 9, 8, 4], [4, 9])

