from data_structure import *
import pdb

def test(sln, nums, k, t, answer):
    print('nums = %s, k = %d, t = %d, answer = %d' % (nums, k, t, answer))
    out = sln.containsNearbyAlmostDuplicate(nums, k, t)
    assert out == answer, out

def run(sln, module):
    test(sln, [1,2,3,1], 3, 0, True)
    test(sln, [1,0,1,1], 1, 2, True)
    test(sln, [1,5,9,1,5,9], 2, 3, False)
