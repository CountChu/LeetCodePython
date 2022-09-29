from data_structure import *
import pdb

def test(sln, nums, target, answer):
    print('nums = %s, target = %d, answer = %d' % (nums, target, answer))
    out = sln.findTargetSumWays(nums, target)
    assert out == answer, out

def run(sln, module):
    test(sln, [1, 1, 1, 1, 1], 3, 5)
    test(sln, [1], 1, 1)
    test(sln, [1, 0], 1, 2)

