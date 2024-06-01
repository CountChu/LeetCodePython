from data_structure import *
import pdb

def test(sln, nums, target, answer):
    print('nums = %s, target = %d, answer = %d' % (nums, target, answer))
    out = sln.findTargetSumWays(nums, target)
    assert out == answer, out

def run(sln):
    test(sln, [1, 1, 1, 1, 1], 3, 5)
    test(sln, [1], 1, 1)
    test(sln, [1, 0], 1, 2)
    test(sln, [19,32,36,7,37,10,44,21,40,39,39,18,5,34,3,40,33,2,46,46], 29, 5715)

